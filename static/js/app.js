const state = {
  recipes: [],
  currentPlan: null,
  editingRecipeId: null,
  expandedMealIds: new Set(),
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
  renderPlan();
});

async function loadLatestPlan() {
  const res = await fetch("/api/plans/latest");
  const plan = await res.json();
  if (plan) {
    state.currentPlan = plan;
    renderPlan();
  }
}

function renderPlan() {
  const container = document.getElementById("plan-meals");
  container.innerHTML = "";

  if (!state.currentPlan) return;

  state.currentPlan.meals.forEach((meal) => {
    const isExpanded = state.expandedMealIds.has(meal.id);
    const ingredientsHtml = meal.recipe.ingredients
      .map((i) => `<li>${i.amount} ${i.unit} ${i.ingredient}</li>`)
      .join("");
    const instructionsHtml = (meal.recipe.instructions || "")
      .split("\n")
      .filter(Boolean)
      .map((line) => `<p>${line}</p>`)
      .join("");

    const card = document.createElement("div");
    card.className = "meal-card";
    card.innerHTML = `
      <div class="meal-summary">
        <div>
          <div class="day">${meal.day_name}</div>
          <h3>${meal.recipe.name}</h3>
          <div class="meta">${meal.recipe.cuisine_type} · ${meal.recipe.cook_time_minutes} min</div>
          <div class="servings-control">
            <label style="margin:0;">Servings</label>
            <input type="number" class="servings-input" min="1" value="${meal.servings}">
          </div>
        </div>
        <button class="view">${isExpanded ? "Hide" : "View"}</button>
      </div>
      <div class="recipe-detail" style="display:${isExpanded ? "block" : "none"};">
        <h4>Ingredients</h4>
        <ul>${ingredientsHtml}</ul>
        <h4>Instructions</h4>
        ${instructionsHtml || "<p class='muted'>No instructions added.</p>"}
      </div>
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
    card.querySelector(".servings-input").addEventListener("change", async (e) => {
      const newServings = parseInt(e.target.value, 10);
      await fetch(`/api/plans/${state.currentPlan.id}/meals/${meal.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ servings_override: newServings }),
      });
      const res = await fetch(`/api/plans/${state.currentPlan.id}`);
      state.currentPlan = await res.json();
      renderPlan();
    });
    container.appendChild(card);
  });
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
