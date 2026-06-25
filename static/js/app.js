const DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

const state = {
  recipes: [],
  currentPlan: null,
  editingRecipeId: null,
  expandedMealIds: new Set(),
  swappingMealKey: null,
};

// ---- Tab navigation ----
document.querySelectorAll(".tab-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
    document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(`tab-${btn.dataset.tab}`).classList.add("active");
  });
});

// ---- Ingredient row builder ----
function addIngredientRow(values = { ingredient: "", amount: "", unit: "" }) {
  const container = document.getElementById("ingredient-rows");
  const row = document.createElement("div");
  row.className = "ingredient-row";
  row.innerHTML = `
    <input type="text" class="ingredient-name" placeholder="ingredient" value="${values.ingredient}">
    <input type="number" class="amount" placeholder="amt" step="0.01" value="${values.amount}">
    <input type="text" class="unit" placeholder="unit" value="${values.unit}">
    <button type="button" class="remove-row">×</button>
  `;
  row.querySelector(".remove-row").addEventListener("click", () => row.remove());
  container.appendChild(row);
}

document.getElementById("add-ingredient-row").addEventListener("click", () => addIngredientRow());

function clearIngredientRows() {
  document.getElementById("ingredient-rows").innerHTML = "";
}

// ---- Recipe form ----
const recipeForm = document.getElementById("recipe-form");

recipeForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const ingredients = [...document.querySelectorAll(".ingredient-row")]
    .map((row) => ({
      ingredient: row.querySelector(".ingredient-name").value.trim(),
      amount: parseFloat(row.querySelector(".amount").value),
      unit: row.querySelector(".unit").value.trim(),
    }))
    .filter((i) => i.ingredient && !isNaN(i.amount) && i.unit);

  const payload = {
    name: document.getElementById("recipe-name").value.trim(),
    cuisine_type: document.getElementById("recipe-cuisine").value.trim(),
    cook_time_minutes: parseInt(document.getElementById("recipe-cook-time").value, 10),
    base_servings: parseInt(document.getElementById("recipe-servings").value, 10),
    instructions: document.getElementById("recipe-instructions").value.trim(),
    tags: document.getElementById("recipe-tags").value
      .split(",")
      .map((t) => t.trim())
      .filter(Boolean),
    ingredients,
  };

  const editingId = document.getElementById("recipe-id").value;
  const url = editingId ? `/api/recipes/${editingId}` : "/api/recipes";
  const method = editingId ? "PUT" : "POST";

  await fetch(url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  resetRecipeForm();
  await loadRecipes();
});

document.getElementById("cancel-edit-btn").addEventListener("click", resetRecipeForm);

function resetRecipeForm() {
  recipeForm.reset();
  document.getElementById("recipe-id").value = "";
  document.getElementById("recipe-form-title").textContent = "Add a Recipe";
  document.getElementById("cancel-edit-btn").style.display = "none";
  clearIngredientRows();
  addIngredientRow();
}

function editRecipe(recipe) {
  document.getElementById("recipe-id").value = recipe.id;
  document.getElementById("recipe-name").value = recipe.name;
  document.getElementById("recipe-cuisine").value = recipe.cuisine_type;
  document.getElementById("recipe-cook-time").value = recipe.cook_time_minutes;
  document.getElementById("recipe-servings").value = recipe.base_servings;
  document.getElementById("recipe-tags").value = recipe.tags.join(", ");
  document.getElementById("recipe-instructions").value = recipe.instructions || "";

  clearIngredientRows();
  recipe.ingredients.forEach((i) => addIngredientRow(i));

  document.getElementById("recipe-form-title").textContent = "Edit Recipe";
  document.getElementById("cancel-edit-btn").style.display = "inline-block";
  document.querySelector('[data-tab="recipes"]').click();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

async function deleteRecipe(id) {
  if (!confirm("Delete this recipe?")) return;
  await fetch(`/api/recipes/${id}`, { method: "DELETE" });
  await loadRecipes();
}

// ---- Recipe list ----
async function loadRecipes() {
  const res = await fetch("/api/recipes");
  state.recipes = await res.json();
  renderRecipeList();
}

function renderRecipeList() {
  const search = document.getElementById("recipe-search").value.toLowerCase();
  const list = document.getElementById("recipe-list");
  list.innerHTML = "";

  state.recipes
    .filter((r) => r.name.toLowerCase().includes(search) || r.cuisine_type.toLowerCase().includes(search))
    .forEach((recipe) => {
      const card = document.createElement("div");
      card.className = "recipe-card-wrapper";
      const ingredientsHtml = recipe.ingredients
        .map((i) => `<li>${i.amount} ${i.unit} ${i.ingredient}</li>`)
        .join("");
      const instructionsHtml = (recipe.instructions || "")
        .split("\n")
        .filter(Boolean)
        .map((line) => `<p>${line}</p>`)
        .join("");

      card.innerHTML = `
        <div class="recipe-card">
          <div class="recipe-summary">
            <strong>${recipe.name}</strong>
            <div class="meta">${recipe.cuisine_type} · ${recipe.cook_time_minutes} min · serves ${recipe.base_servings}</div>
            <div class="tags">${recipe.tags.map((t) => `<span class="tag-chip">${t}</span>`).join("")}</div>
          </div>
          <div class="actions">
            <button class="view">View</button>
            <button class="edit">Edit</button>
            <button class="delete">Delete</button>
          </div>
        </div>
        <div class="recipe-detail" style="display:none;">
          <h4>Ingredients</h4>
          <ul>${ingredientsHtml}</ul>
          <h4>Instructions</h4>
          ${instructionsHtml || "<p class='muted'>No instructions added.</p>"}
        </div>
      `;
      const detail = card.querySelector(".recipe-detail");
      card.querySelector(".view").addEventListener("click", () => {
        detail.style.display = detail.style.display === "none" ? "block" : "none";
      });
      card.querySelector(".edit").addEventListener("click", () => editRecipe(recipe));
      card.querySelector(".delete").addEventListener("click", () => deleteRecipe(recipe.id));
      list.appendChild(card);
    });
}

document.getElementById("recipe-search").addEventListener("input", renderRecipeList);

// ---- Weekly plan ----
document.getElementById("generate-plan-btn").addEventListener("click", async () => {
  if (state.currentPlan && state.currentPlan.meals.length > 0) {
    const confirmed = confirm(
      "This will replace your current plan with a new shuffle. Your old plan stays in history and can be restored, but continue?"
    );
    if (!confirmed) return;
  }

  const excludeTags = document.getElementById("exclude-tags-input").value
    .split(",")
    .map((t) => t.trim().toLowerCase())
    .filter(Boolean);

  const res = await fetch("/api/plans/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ exclude_tags: excludeTags }),
  });

  if (!res.ok) {
    const err = await res.json();
    alert(err.error || "Could not generate plan");
    return;
  }

  state.currentPlan = await res.json();
  state.expandedMealIds.clear();
  state.swappingMealKey = null;
  renderPlan();
  loadPlanHistory();
});

async function loadLatestPlan() {
  const res = await fetch("/api/plans/latest");
  const plan = await res.json();
  if (plan) {
    state.currentPlan = plan;
    renderPlan();
  }
}

async function refreshCurrentPlan() {
  const res = await fetch(`/api/plans/${state.currentPlan.id}`);
  state.currentPlan = await res.json();
  renderPlan();
}

async function swapMealRecipe(dayOfWeek, meal, newRecipeId) {
  if (meal) {
    await fetch(`/api/plans/${state.currentPlan.id}/meals/${meal.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ recipe_id: parseInt(newRecipeId, 10) }),
    });
  } else {
    await fetch(`/api/plans/${state.currentPlan.id}/meals`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ day_of_week: dayOfWeek, recipe_id: parseInt(newRecipeId, 10) }),
    });
  }
  state.swappingMealKey = null;
  await refreshCurrentPlan();
}

function buildRecipePicker(dayOfWeek, meal, usedRecipeIds) {
  const select = document.createElement("select");
  const placeholder = document.createElement("option");
  placeholder.value = "";
  placeholder.textContent = "Choose a recipe...";
  select.appendChild(placeholder);

  state.recipes
    .slice()
    .sort((a, b) => a.name.localeCompare(b.name))
    .forEach((recipe) => {
      const option = document.createElement("option");
      option.value = recipe.id;
      const inUseElsewhere = usedRecipeIds.has(recipe.id) && (!meal || meal.recipe.id !== recipe.id);
      option.textContent = `${recipe.name} (${recipe.cuisine_type})${inUseElsewhere ? " — already this week" : ""}`;
      select.appendChild(option);
    });

  select.addEventListener("change", () => {
    if (select.value) swapMealRecipe(dayOfWeek, meal, select.value);
  });
  return select;
}

function renderPlan() {
  const container = document.getElementById("plan-meals");
  container.innerHTML = "";

  if (!state.currentPlan) return;

  const mealsByDay = {};
  state.currentPlan.meals.forEach((meal) => {
    mealsByDay[meal.day_of_week] = meal;
  });
  const usedRecipeIds = new Set(state.currentPlan.meals.map((m) => m.recipe.id));

  DAY_NAMES.forEach((dayName, dayOfWeek) => {
    const meal = mealsByDay[dayOfWeek];
    const card = document.createElement("div");
    card.className = "meal-card";

    if (!meal) {
      card.innerHTML = `<div class="day">${dayName}</div><p class="muted">No meal picked for this day yet.</p><div class="swap-picker"></div>`;
      card.querySelector(".swap-picker").appendChild(buildRecipePicker(dayOfWeek, null, usedRecipeIds));
      container.appendChild(card);
      return;
    }

    const mealKey = `${dayOfWeek}`;
    const isExpanded = state.expandedMealIds.has(meal.id);
    const isSwapping = state.swappingMealKey === mealKey;
    const ingredientsHtml = meal.recipe.ingredients
      .map((i) => `<li>${i.amount} ${i.unit} ${i.ingredient}</li>`)
      .join("");
    const instructionsHtml = (meal.recipe.instructions || "")
      .split("\n")
      .filter(Boolean)
      .map((line) => `<p>${line}</p>`)
      .join("");

    card.innerHTML = `
      <div class="meal-summary">
        <div>
          <div class="day">${dayName}</div>
          <h3>${meal.recipe.name}</h3>
          <div class="meta">${meal.recipe.cuisine_type} · ${meal.recipe.cook_time_minutes} min</div>
          <div class="servings-control">
            <label style="margin:0;">Servings</label>
            <input type="number" class="servings-input" min="1" value="${meal.servings}">
          </div>
        </div>
        <div class="meal-actions">
          <button class="view">${isExpanded ? "Hide" : "View"}</button>
          <button class="swap">${isSwapping ? "Cancel" : "Swap"}</button>
        </div>
      </div>
      <div class="recipe-detail" style="display:${isExpanded ? "block" : "none"};">
        <h4>Ingredients</h4>
        <ul>${ingredientsHtml}</ul>
        <h4>Instructions</h4>
        ${instructionsHtml || "<p class='muted'>No instructions added.</p>"}
      </div>
      <div class="swap-picker" style="display:${isSwapping ? "block" : "none"};"></div>
    `;
    card.querySelector(".view").addEventListener("click", (e) => {
      const detail = card.querySelector(".recipe-detail");
      const nowExpanded = detail.style.display === "none";
      detail.style.display = nowExpanded ? "block" : "none";
      e.target.textContent = nowExpanded ? "Hide" : "View";
      if (nowExpanded) {
        state.expandedMealIds.add(meal.id);
      } else {
        state.expandedMealIds.delete(meal.id);
      }
    });
    card.querySelector(".swap").addEventListener("click", (e) => {
      state.swappingMealKey = isSwapping ? null : mealKey;
      renderPlan();
    });
    if (isSwapping) {
      const pickerContainer = card.querySelector(".swap-picker");
      pickerContainer.appendChild(buildRecipePicker(dayOfWeek, meal, usedRecipeIds));
    }
    card.querySelector(".servings-input").addEventListener("change", async (e) => {
      const newServings = parseInt(e.target.value, 10);
      await fetch(`/api/plans/${state.currentPlan.id}/meals/${meal.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ servings_override: newServings }),
      });
      await refreshCurrentPlan();
    });
    container.appendChild(card);
  });
}

// ---- Plan history / rollback ----
document.getElementById("toggle-history-btn").addEventListener("click", async () => {
  const panel = document.getElementById("plan-history");
  const showing = panel.style.display === "none";
  panel.style.display = showing ? "block" : "none";
  if (showing) await loadPlanHistory();
});

async function loadPlanHistory() {
  const res = await fetch("/api/plans/history?limit=10");
  const plans = await res.json();
  renderPlanHistory(plans);
}

function renderPlanHistory(plans) {
  const panel = document.getElementById("plan-history");
  panel.innerHTML = "";

  if (plans.length === 0) {
    panel.innerHTML = "<p class='muted'>No past plans yet.</p>";
    return;
  }

  const ul = document.createElement("ul");
  ul.className = "history-list";
  plans.forEach((plan) => {
    const li = document.createElement("li");
    const when = new Date(plan.created_at).toLocaleString([], {
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "2-digit",
    });
    li.innerHTML = `
      <div>
        <div class="history-meta">${when}${plan.active ? " · <strong>current</strong>" : ""}</div>
        <div class="history-recipes">${plan.recipe_names.join(", ") || "(empty)"}</div>
      </div>
    `;
    if (!plan.active) {
      const restoreBtn = document.createElement("button");
      restoreBtn.textContent = "Restore";
      restoreBtn.className = "btn-secondary btn-small";
      restoreBtn.addEventListener("click", async () => {
        if (!confirm("Restore this plan as the current week's plan?")) return;
        const res = await fetch(`/api/plans/${plan.id}/activate`, { method: "POST" });
        state.currentPlan = await res.json();
        state.expandedMealIds.clear();
        state.swappingMealKey = null;
        renderPlan();
        await loadPlanHistory();
      });
      li.appendChild(restoreBtn);
    }
    ul.appendChild(li);
  });
  panel.appendChild(ul);
}

// ---- Grocery list ----
document.getElementById("generate-grocery-btn").addEventListener("click", async () => {
  if (!state.currentPlan) {
    alert("Generate a weekly plan first.");
    return;
  }
  const res = await fetch(`/api/plans/${state.currentPlan.id}/grocery-list`, { method: "POST" });
  const groceryList = await res.json();
  cacheGroceryListForOffline(groceryList);
  renderGroceryList(groceryList);
});

function renderGroceryList(groceryList) {
  const container = document.getElementById("grocery-items");
  container.innerHTML = "";

  // Backend already returns items sorted by store-section order, then name.
  const groups = [];
  groceryList.items.forEach((item) => {
    let group = groups.find((g) => g.category === item.category);
    if (!group) {
      group = { category: item.category, items: [] };
      groups.push(group);
    }
    group.items.push(item);
  });

  groups.forEach((group) => {
    const section = document.createElement("div");
    section.className = "grocery-section";

    const heading = document.createElement("h3");
    heading.className = "grocery-category";
    heading.textContent = group.category;
    section.appendChild(heading);

    const ul = document.createElement("ul");
    group.items.forEach((item) => {
      const li = document.createElement("li");
      if (item.checked) li.classList.add("checked");
      li.innerHTML = `
        <input type="checkbox" ${item.checked ? "checked" : ""}>
        <span>${item.amount} ${item.unit} ${item.ingredient}</span>
      `;
      li.querySelector("input").addEventListener("change", async (e) => {
        await fetch(`/api/grocery-lists/${groceryList.id}/items/${item.id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ checked: e.target.checked }),
        });
        li.classList.toggle("checked", e.target.checked);
      });
      ul.appendChild(li);
    });
    section.appendChild(ul);
    container.appendChild(section);
  });
}

function cacheGroceryListForOffline(groceryList) {
  localStorage.setItem("dinnerdeck_grocery_list", JSON.stringify(groceryList));
  if (state.currentPlan) {
    localStorage.setItem("dinnerdeck_plan", JSON.stringify(state.currentPlan));
  }
}

function loadCachedGroceryList() {
  const cached = localStorage.getItem("dinnerdeck_grocery_list");
  if (cached) renderGroceryList(JSON.parse(cached));
}

// ---- Init ----
resetRecipeForm();
loadRecipes();
loadLatestPlan();
loadCachedGroceryList();

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/sw.js").catch((err) => console.error("SW registration failed", err));
}
