RECIPES = []


def r(name, cuisine, cook_time, ingredients, instructions, tags):
    RECIPES.append({
        "name": name,
        "cuisine_type": cuisine,
        "cook_time_minutes": cook_time,
        "base_servings": 4,
        "instructions": instructions,
        "tags": tags,
        "ingredients": [
            {"ingredient": i, "amount": a, "unit": u} for (i, a, u) in ingredients
        ],
    })


# ---------------- ASIAN (25) ----------------

r("Chicken Teriyaki Stir-Fry", "Asian", 25,
  [("chicken breast", 1, "lb"), ("broccoli", 2, "cup"), ("carrot", 1, "cup"),
   ("soy sauce", 3, "tbsp"), ("honey", 2, "tbsp"), ("garlic", 2, "clove"), ("rice", 2, "cup")],
  "1. Cook rice.\n2. Cube chicken and stir-fry until browned.\n3. Add vegetables, cook 5 min.\n4. Stir in soy sauce, honey, garlic.\n5. Serve over rice.",
  ["chicken", "gluten", "soy"])

r("Beef and Broccoli", "Asian", 20,
  [("flank steak", 1, "lb"), ("broccoli", 3, "cup"), ("soy sauce", 3, "tbsp"),
   ("cornstarch", 1, "tbsp"), ("garlic", 2, "clove"), ("ginger", 1, "tsp"), ("rice", 2, "cup")],
  "1. Slice beef thin.\n2. Sear beef 2-3 min, set aside.\n3. Stir-fry broccoli with garlic and ginger.\n4. Combine with sauce and beef, simmer 3 min.\n5. Serve over rice.",
  ["beef", "soy", "gluten"])

r("Shrimp Pad Thai", "Asian", 25,
  [("shrimp", 1, "lb"), ("rice noodles", 8, "oz"), ("egg", 2, "each"),
   ("bean sprouts", 1, "cup"), ("peanuts", 0.25, "cup"), ("lime", 1, "each"), ("fish sauce", 2, "tbsp")],
  "1. Soak noodles per package.\n2. Scramble eggs, set aside.\n3. Stir-fry shrimp until pink.\n4. Add noodles, sauce, sprouts, eggs.\n5. Top with peanuts and lime.",
  ["shrimp", "shellfish", "peanuts", "fish"])

r("Vegetable Fried Rice", "Asian", 15,
  [("rice", 3, "cup"), ("egg", 2, "each"), ("frozen peas and carrots", 1, "cup"),
   ("soy sauce", 2, "tbsp"), ("green onion", 2, "each"), ("sesame oil", 1, "tsp")],
  "1. Scramble eggs in pan, remove.\n2. Stir-fry vegetables 3 min.\n3. Add rice, soy sauce, eggs back in.\n4. Toss with sesame oil and green onion.",
  ["vegetarian", "soy", "gluten"])

r("Chicken Fried Rice", "Asian", 20,
  [("chicken breast", 0.75, "lb"), ("rice", 3, "cup"), ("egg", 2, "each"),
   ("frozen peas and carrots", 1, "cup"), ("soy sauce", 2, "tbsp"), ("green onion", 2, "each")],
  "1. Dice and cook chicken through.\n2. Scramble eggs, set aside.\n3. Stir-fry vegetables.\n4. Combine rice, chicken, eggs, soy sauce.\n5. Garnish with green onion.",
  ["chicken", "soy", "gluten"])

r("Honey Garlic Salmon", "Asian", 20,
  [("salmon fillet", 1, "lb"), ("honey", 3, "tbsp"), ("soy sauce", 2, "tbsp"),
   ("garlic", 3, "clove"), ("rice", 2, "cup"), ("broccoli", 2, "cup")],
  "1. Whisk honey, soy sauce, garlic.\n2. Sear salmon 3 min per side.\n3. Add sauce, simmer 2 min.\n4. Steam broccoli.\n5. Serve over rice.",
  ["fish", "soy", "gluten"])

r("Korean Beef Bowl", "Asian", 20,
  [("ground beef", 1, "lb"), ("soy sauce", 3, "tbsp"), ("brown sugar", 2, "tbsp"),
   ("garlic", 2, "clove"), ("ginger", 1, "tsp"), ("rice", 2, "cup"), ("green onion", 2, "each")],
  "1. Brown ground beef.\n2. Add soy sauce, sugar, garlic, ginger.\n3. Simmer 5 min.\n4. Serve over rice with green onion.",
  ["beef", "soy", "gluten"])

r("Chicken Lo Mein", "Asian", 20,
  [("chicken breast", 0.75, "lb"), ("lo mein noodles", 8, "oz"), ("cabbage", 2, "cup"),
   ("carrot", 1, "cup"), ("soy sauce", 3, "tbsp"), ("garlic", 2, "clove")],
  "1. Boil noodles, drain.\n2. Stir-fry chicken until cooked.\n3. Add vegetables and garlic.\n4. Toss in noodles and soy sauce.",
  ["chicken", "soy", "gluten"])

r("Tofu Vegetable Stir-Fry", "Asian", 20,
  [("tofu", 14, "oz"), ("bell pepper", 1, "cup"), ("broccoli", 2, "cup"),
   ("soy sauce", 3, "tbsp"), ("garlic", 2, "clove"), ("rice", 2, "cup")],
  "1. Press and cube tofu, pan-fry until golden.\n2. Stir-fry vegetables with garlic.\n3. Combine with tofu and soy sauce.\n4. Serve over rice.",
  ["vegetarian", "soy", "gluten"])

r("Shrimp Fried Rice", "Asian", 20,
  [("shrimp", 1, "lb"), ("rice", 3, "cup"), ("egg", 2, "each"),
   ("frozen peas and carrots", 1, "cup"), ("soy sauce", 2, "tbsp")],
  "1. Cook shrimp until pink, set aside.\n2. Scramble eggs.\n3. Stir-fry vegetables, add rice.\n4. Combine all with soy sauce.",
  ["shrimp", "shellfish", "soy", "gluten"])

r("General Tso's Chicken (Lightened Up)", "Asian", 25,
  [("chicken breast", 1, "lb"), ("cornstarch", 2, "tbsp"), ("soy sauce", 3, "tbsp"),
   ("honey", 2, "tbsp"), ("garlic", 2, "clove"), ("rice vinegar", 1, "tbsp"), ("rice", 2, "cup")],
  "1. Coat chicken in cornstarch, pan-fry until crisp.\n2. Whisk soy sauce, honey, garlic, vinegar.\n3. Toss chicken in sauce, simmer 2 min.\n4. Serve over rice.",
  ["chicken", "soy", "gluten"])

r("Sesame Noodles with Chicken", "Asian", 20,
  [("chicken breast", 0.75, "lb"), ("spaghetti", 8, "oz"), ("sesame oil", 2, "tbsp"),
   ("soy sauce", 3, "tbsp"), ("peanut butter", 1, "tbsp"), ("green onion", 2, "each")],
  "1. Boil noodles, drain.\n2. Cook chicken, slice.\n3. Whisk sesame oil, soy sauce, peanut butter.\n4. Toss noodles, chicken, sauce, top with onion.",
  ["chicken", "peanuts", "gluten", "soy"])

r("Veggie Spring Roll Bowl", "Asian", 15,
  [("rice noodles", 8, "oz"), ("carrot", 1, "cup"), ("cucumber", 1, "cup"),
   ("cabbage", 2, "cup"), ("peanut sauce", 0.25, "cup"), ("cilantro", 0.25, "cup")],
  "1. Cook rice noodles, drain.\n2. Julienne vegetables.\n3. Combine noodles and vegetables in bowls.\n4. Top with peanut sauce and cilantro.",
  ["vegetarian", "peanuts"])

r("Chicken Satay Skewers", "Asian", 25,
  [("chicken breast", 1, "lb"), ("peanut butter", 0.25, "cup"), ("soy sauce", 2, "tbsp"),
   ("lime", 1, "each"), ("garlic", 2, "clove"), ("rice", 2, "cup")],
  "1. Cube chicken, thread onto skewers.\n2. Grill or pan-cook until done.\n3. Whisk peanut butter, soy sauce, lime, garlic for sauce.\n4. Serve skewers with sauce over rice.",
  ["chicken", "peanuts", "soy"])

r("Mongolian Beef", "Asian", 20,
  [("flank steak", 1, "lb"), ("cornstarch", 2, "tbsp"), ("soy sauce", 4, "tbsp"),
   ("brown sugar", 2, "tbsp"), ("garlic", 2, "clove"), ("green onion", 3, "each"), ("rice", 2, "cup")],
  "1. Coat beef in cornstarch, sear until crisp.\n2. Combine soy sauce, sugar, garlic in pan.\n3. Add beef back, toss to coat.\n4. Top with green onion, serve over rice.",
  ["beef", "soy", "gluten"])

r("Chicken Pho (Quick)", "Asian", 28,
  [("chicken breast", 1, "lb"), ("chicken broth", 6, "cup"), ("rice noodles", 8, "oz"),
   ("bean sprouts", 1, "cup"), ("lime", 1, "each"), ("cilantro", 0.25, "cup"), ("ginger", 1, "tsp")],
  "1. Simmer broth with ginger 10 min.\n2. Poach chicken in broth until cooked, slice.\n3. Cook noodles separately.\n4. Assemble bowls with noodles, broth, chicken, sprouts, lime, cilantro.",
  ["chicken", "gluten"])

r("Garlic Soy Tilapia", "Asian", 18,
  [("tilapia fillet", 1, "lb"), ("soy sauce", 2, "tbsp"), ("garlic", 3, "clove"),
   ("lime", 1, "each"), ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Pan-sear tilapia 3 min per side.\n2. Add soy sauce, garlic, lime, simmer 2 min.\n3. Steam green beans.\n4. Serve fish over rice with beans.",
  ["fish", "soy", "gluten"])

r("Kung Pao Chicken", "Asian", 22,
  [("chicken breast", 1, "lb"), ("peanuts", 0.33, "cup"), ("bell pepper", 1, "cup"),
   ("soy sauce", 3, "tbsp"), ("rice vinegar", 1, "tbsp"), ("garlic", 2, "clove"), ("rice", 2, "cup")],
  "1. Cube and stir-fry chicken until cooked.\n2. Add bell pepper and garlic.\n3. Stir in soy sauce, vinegar, peanuts.\n4. Serve over rice.",
  ["chicken", "peanuts", "soy", "gluten"])

r("Edamame Soba Noodle Bowl", "Asian", 18,
  [("soba noodles", 8, "oz"), ("edamame", 1, "cup"), ("carrot", 1, "cup"),
   ("soy sauce", 2, "tbsp"), ("sesame oil", 1, "tbsp"), ("green onion", 2, "each")],
  "1. Cook soba noodles, drain and cool slightly.\n2. Steam edamame.\n3. Toss noodles with edamame, carrot, soy sauce, sesame oil.\n4. Top with green onion.",
  ["vegetarian", "soy", "gluten"])

r("Teriyaki Salmon Bowl", "Asian", 20,
  [("salmon fillet", 1, "lb"), ("soy sauce", 3, "tbsp"), ("honey", 2, "tbsp"),
   ("rice", 2, "cup"), ("cucumber", 1, "cup"), ("avocado", 1, "each")],
  "1. Whisk soy sauce and honey.\n2. Sear salmon, baste with sauce 3 min.\n3. Slice cucumber and avocado.\n4. Build bowl with rice, salmon, vegetables.",
  ["fish", "soy", "gluten"])

r("Chicken Chow Mein", "Asian", 20,
  [("chicken breast", 0.75, "lb"), ("chow mein noodles", 8, "oz"), ("cabbage", 2, "cup"),
   ("carrot", 1, "cup"), ("soy sauce", 3, "tbsp"), ("garlic", 2, "clove")],
  "1. Boil noodles, drain.\n2. Stir-fry chicken until done.\n3. Add vegetables and garlic.\n4. Toss in noodles and soy sauce.",
  ["chicken", "soy", "gluten"])

r("Thai Basil Ground Turkey", "Asian", 18,
  [("ground turkey", 1, "lb"), ("basil", 0.5, "cup"), ("soy sauce", 2, "tbsp"),
   ("fish sauce", 1, "tbsp"), ("garlic", 3, "clove"), ("rice", 2, "cup")],
  "1. Brown ground turkey with garlic.\n2. Stir in soy sauce and fish sauce.\n3. Remove from heat, fold in basil.\n4. Serve over rice.",
  ["fish", "soy", "gluten"])

r("Egg Drop Soup with Dumplings", "Asian", 20,
  [("chicken broth", 6, "cup"), ("egg", 3, "each"), ("frozen dumplings", 16, "each"),
   ("green onion", 2, "each"), ("soy sauce", 1, "tbsp")],
  "1. Bring broth to simmer, add dumplings, cook per package.\n2. Whisk eggs, drizzle into simmering broth.\n3. Stir gently to form ribbons.\n4. Season with soy sauce, top with green onion.",
  ["gluten", "soy"])

r("Cashew Chicken", "Asian", 20,
  [("chicken breast", 1, "lb"), ("cashews", 0.5, "cup"), ("bell pepper", 1, "cup"),
   ("soy sauce", 3, "tbsp"), ("garlic", 2, "clove"), ("rice", 2, "cup")],
  "1. Cube and stir-fry chicken until cooked.\n2. Add bell pepper and garlic.\n3. Stir in soy sauce and cashews.\n4. Serve over rice.",
  ["chicken", "tree nuts", "soy", "gluten"])

r("Vegetable Dumpling Stir-Fry", "Asian", 15,
  [("frozen dumplings", 20, "each"), ("bok choy", 2, "cup"), ("soy sauce", 2, "tbsp"),
   ("garlic", 2, "clove"), ("sesame oil", 1, "tsp")],
  "1. Pan-fry dumplings until golden.\n2. Stir-fry bok choy and garlic.\n3. Combine with soy sauce and sesame oil.\n4. Serve together.",
  ["vegetarian", "gluten", "soy"])

r("Spicy Tuna Rice Bowl", "Asian", 15,
  [("canned tuna", 10, "oz"), ("rice", 2, "cup"), ("sriracha", 2, "tbsp"),
   ("mayonnaise", 2, "tbsp"), ("cucumber", 1, "cup"), ("green onion", 2, "each")],
  "1. Cook rice.\n2. Mix tuna with sriracha and mayo.\n3. Slice cucumber.\n4. Build bowl with rice, tuna mix, cucumber, green onion.",
  ["fish", "spicy"])

# ---------------- TEX-MEX (25) ----------------

r("Chicken Fajitas", "Tex-Mex", 25,
  [("chicken breast", 1, "lb"), ("bell pepper", 2, "cup"), ("onion", 1, "cup"),
   ("taco seasoning", 2, "tbsp"), ("tortillas", 8, "each"), ("lime", 1, "each")],
  "1. Slice chicken and vegetables.\n2. Saute chicken until browned.\n3. Add peppers, onion, seasoning, cook 5 min.\n4. Squeeze lime, serve with tortillas.",
  ["chicken", "gluten"])

r("Beef Tacos", "Tex-Mex", 20,
  [("ground beef", 1, "lb"), ("taco seasoning", 2, "tbsp"), ("tortillas", 8, "each"),
   ("lettuce", 1, "cup"), ("tomato", 1, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Brown ground beef.\n2. Stir in taco seasoning and a splash of water.\n3. Warm tortillas.\n4. Assemble tacos with toppings.",
  ["beef", "dairy", "gluten"])

r("Black Bean and Corn Quesadillas", "Tex-Mex", 15,
  [("black beans", 15, "oz"), ("corn", 1, "cup"), ("cheddar cheese", 1.5, "cup"),
   ("tortillas", 8, "each"), ("salsa", 0.5, "cup")],
  "1. Mix beans, corn, cheese.\n2. Spread on tortillas, fold.\n3. Cook in skillet until golden and cheese melts.\n4. Serve with salsa.",
  ["vegetarian", "dairy", "gluten"])

r("Shrimp Tacos with Slaw", "Tex-Mex", 20,
  [("shrimp", 1, "lb"), ("cabbage", 2, "cup"), ("lime", 1, "each"),
   ("mayonnaise", 2, "tbsp"), ("tortillas", 8, "each"), ("taco seasoning", 1, "tbsp")],
  "1. Season and saute shrimp until pink.\n2. Toss cabbage with mayo and lime for slaw.\n3. Warm tortillas.\n4. Assemble tacos with shrimp and slaw.",
  ["shrimp", "shellfish", "gluten"])

r("Chicken Enchiladas", "Tex-Mex", 28,
  [("chicken breast", 1, "lb"), ("enchilada sauce", 2, "cup"), ("tortillas", 8, "each"),
   ("cheddar cheese", 1.5, "cup"), ("onion", 0.5, "cup")],
  "1. Cook and shred chicken.\n2. Mix with onion and a little sauce.\n3. Roll into tortillas, place in dish, top with remaining sauce and cheese.\n4. Bake 15 min at 400F.",
  ["chicken", "dairy", "gluten"])

r("Tex-Mex Rice Bowl", "Tex-Mex", 20,
  [("ground turkey", 1, "lb"), ("rice", 2, "cup"), ("black beans", 15, "oz"),
   ("corn", 1, "cup"), ("salsa", 0.5, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Cook rice.\n2. Brown ground turkey with taco seasoning.\n3. Warm beans and corn.\n4. Build bowls with rice, turkey, beans, corn, salsa, cheese.",
  ["dairy"])

r("Beef and Bean Burritos", "Tex-Mex", 20,
  [("ground beef", 1, "lb"), ("pinto beans", 15, "oz"), ("rice", 1, "cup"),
   ("tortillas", 6, "each"), ("cheddar cheese", 1, "cup"), ("salsa", 0.5, "cup")],
  "1. Brown ground beef.\n2. Warm beans and rice.\n3. Layer beef, beans, rice, cheese on tortillas.\n4. Roll and serve with salsa.",
  ["beef", "dairy", "gluten"])

r("Chicken Taco Salad", "Tex-Mex", 20,
  [("chicken breast", 1, "lb"), ("lettuce", 3, "cup"), ("black beans", 15, "oz"),
   ("corn", 1, "cup"), ("tortilla chips", 1, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Season and cook chicken, slice.\n2. Toss lettuce with beans and corn.\n3. Top with chicken, cheese, crushed chips.",
  ["dairy", "gluten"])

r("Shrimp and Black Bean Tacos", "Tex-Mex", 18,
  [("shrimp", 1, "lb"), ("black beans", 15, "oz"), ("tortillas", 8, "each"),
   ("avocado", 1, "each"), ("lime", 1, "each"), ("cilantro", 0.25, "cup")],
  "1. Saute shrimp with lime until pink.\n2. Warm black beans.\n3. Assemble tacos with shrimp, beans, avocado, cilantro.",
  ["shrimp", "shellfish", "gluten"])

r("Turkey Taco Skillet", "Tex-Mex", 20,
  [("ground turkey", 1, "lb"), ("taco seasoning", 2, "tbsp"), ("rice", 1, "cup"),
   ("black beans", 15, "oz"), ("tomato", 1, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Brown turkey with seasoning.\n2. Stir in rice, beans, tomato, and water; simmer 10 min.\n3. Top with cheese, melt and serve.",
  ["dairy"])

r("Chicken Quesadillas", "Tex-Mex", 18,
  [("chicken breast", 1, "lb"), ("cheddar cheese", 1.5, "cup"), ("tortillas", 8, "each"),
   ("bell pepper", 1, "cup"), ("salsa", 0.5, "cup")],
  "1. Cook and slice chicken.\n2. Layer chicken, cheese, peppers in tortillas.\n3. Cook in skillet until golden.\n4. Serve with salsa.",
  ["chicken", "dairy", "gluten"])

r("Beef Burrito Bowls", "Tex-Mex", 20,
  [("ground beef", 1, "lb"), ("rice", 2, "cup"), ("black beans", 15, "oz"),
   ("corn", 1, "cup"), ("lettuce", 1, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Cook rice.\n2. Brown beef with taco seasoning.\n3. Warm beans and corn.\n4. Build bowls with all components.",
  ["beef", "dairy"])

r("Pork Carnitas Tacos", "Tex-Mex", 25,
  [("pork tenderloin", 1, "lb"), ("lime", 1, "each"), ("cumin", 1, "tsp"),
   ("tortillas", 8, "each"), ("onion", 0.5, "cup"), ("cilantro", 0.25, "cup")],
  "1. Slice pork thin, season with cumin.\n2. Sear until cooked through, about 8 min.\n3. Squeeze lime over pork.\n4. Serve in tortillas with onion and cilantro.",
  ["pork", "gluten"])

r("Veggie Fajita Bowls", "Tex-Mex", 20,
  [("bell pepper", 2, "cup"), ("onion", 1, "cup"), ("black beans", 15, "oz"),
   ("rice", 2, "cup"), ("taco seasoning", 1, "tbsp"), ("cheddar cheese", 1, "cup")],
  "1. Cook rice.\n2. Saute peppers and onion with seasoning.\n3. Warm black beans.\n4. Build bowls with rice, vegetables, beans, cheese.",
  ["vegetarian", "dairy"])

r("Chicken Tortilla Soup", "Tex-Mex", 25,
  [("chicken breast", 1, "lb"), ("chicken broth", 6, "cup"), ("black beans", 15, "oz"),
   ("corn", 1, "cup"), ("tomato", 1, "cup"), ("tortilla chips", 1, "cup")],
  "1. Poach chicken in broth until cooked, shred.\n2. Add beans, corn, tomato, simmer 10 min.\n3. Serve topped with crushed tortilla chips.",
  ["chicken", "gluten"])

r("Steak Fajita Bowls", "Tex-Mex", 22,
  [("flank steak", 1, "lb"), ("bell pepper", 2, "cup"), ("onion", 1, "cup"),
   ("rice", 2, "cup"), ("taco seasoning", 1, "tbsp"), ("lime", 1, "each")],
  "1. Slice and sear steak, set aside.\n2. Saute peppers and onion with seasoning.\n3. Cook rice.\n4. Build bowls with rice, steak, vegetables, lime.",
  ["beef"])

r("Bean and Cheese Burritos", "Tex-Mex", 12,
  [("pinto beans", 15, "oz"), ("cheddar cheese", 1.5, "cup"), ("tortillas", 6, "each"),
   ("salsa", 0.5, "cup")],
  "1. Warm beans, mash slightly.\n2. Spread beans and cheese on tortillas.\n3. Roll and warm in skillet until cheese melts.\n4. Serve with salsa.",
  ["vegetarian", "dairy", "gluten"])

r("Chicken Chili", "Tex-Mex", 28,
  [("chicken breast", 1, "lb"), ("white beans", 15, "oz"), ("chicken broth", 3, "cup"),
   ("corn", 1, "cup"), ("cumin", 1, "tsp"), ("cheddar cheese", 0.5, "cup")],
  "1. Cook and shred chicken.\n2. Combine with beans, broth, corn, cumin in pot.\n3. Simmer 15 min.\n4. Top with cheese.",
  ["chicken", "dairy"])

r("Salsa Chicken with Rice", "Tex-Mex", 22,
  [("chicken breast", 1, "lb"), ("salsa", 1, "cup"), ("rice", 2, "cup"),
   ("black beans", 15, "oz"), ("cheddar cheese", 1, "cup")],
  "1. Cook chicken in skillet, top with salsa, simmer 5 min.\n2. Cook rice.\n3. Warm black beans.\n4. Serve chicken over rice and beans, top with cheese.",
  ["chicken", "dairy"])

r("Ground Beef Nachos", "Tex-Mex", 18,
  [("ground beef", 1, "lb"), ("tortilla chips", 4, "cup"), ("cheddar cheese", 1.5, "cup"),
   ("black beans", 15, "oz"), ("salsa", 0.5, "cup")],
  "1. Brown ground beef with taco seasoning.\n2. Layer chips, beef, beans, cheese on a sheet pan.\n3. Bake at 400F until cheese melts, 5-7 min.\n4. Top with salsa.",
  ["beef", "dairy", "gluten"])

r("Chicken and Black Bean Burrito Bowls", "Tex-Mex", 20,
  [("chicken breast", 1, "lb"), ("black beans", 15, "oz"), ("rice", 2, "cup"),
   ("corn", 1, "cup"), ("avocado", 1, "each"), ("lime", 1, "each")],
  "1. Season and cook chicken, slice.\n2. Cook rice.\n3. Warm beans and corn.\n4. Build bowls topped with avocado and lime.",
  ["chicken"])

r("Turkey Taco Lettuce Wraps", "Tex-Mex", 15,
  [("ground turkey", 1, "lb"), ("taco seasoning", 2, "tbsp"), ("lettuce", 8, "leaf"),
   ("tomato", 1, "cup"), ("cheddar cheese", 1, "cup")],
  "1. Brown turkey with taco seasoning.\n2. Spoon into lettuce leaves.\n3. Top with tomato and cheese.",
  ["dairy"])

r("Cheesy Beef Enchilada Skillet", "Tex-Mex", 25,
  [("ground beef", 1, "lb"), ("enchilada sauce", 2, "cup"), ("tortillas", 6, "each"),
   ("cheddar cheese", 1.5, "cup"), ("onion", 0.5, "cup")],
  "1. Brown beef with onion.\n2. Tear tortillas, layer with beef and sauce in skillet.\n3. Top with cheese.\n4. Cover and simmer until cheese melts, 5 min.",
  ["beef", "dairy", "gluten"])

r("Shrimp Ceviche Tostadas", "Tex-Mex", 20,
  [("shrimp", 1, "lb"), ("lime", 2, "each"), ("tomato", 1, "cup"),
   ("onion", 0.5, "cup"), ("cilantro", 0.25, "cup"), ("tostada shells", 8, "each")],
  "1. Cook shrimp briefly in boiling water, chop.\n2. Toss with lime, tomato, onion, cilantro.\n3. Chill 10 min if time allows.\n4. Serve on tostada shells.",
  ["shrimp", "shellfish"])

r("Cheesy Chicken Taquitos", "Tex-Mex", 22,
  [("chicken breast", 1, "lb"), ("cheddar cheese", 1, "cup"), ("tortillas", 10, "each"),
   ("taco seasoning", 1, "tbsp"), ("salsa", 0.5, "cup")],
  "1. Cook and shred chicken with seasoning.\n2. Mix with cheese, roll tightly in small tortillas.\n3. Pan-fry seam-side down until golden and crisp.\n4. Serve with salsa.",
  ["chicken", "dairy", "gluten"])

# ---------------- MEDITERRANEAN (25) ----------------

r("Greek Chicken Skewers", "Mediterranean", 25,
  [("chicken breast", 1, "lb"), ("lemon", 1, "each"), ("olive oil", 2, "tbsp"),
   ("garlic", 2, "clove"), ("oregano", 1, "tsp"), ("rice", 2, "cup")],
  "1. Cube chicken, marinate in lemon, oil, garlic, oregano.\n2. Skewer and grill or pan-cook until done.\n3. Serve over rice.",
  ["chicken"])

r("Mediterranean Chickpea Salad", "Mediterranean", 12,
  [("chickpeas", 15, "oz"), ("cucumber", 1, "cup"), ("tomato", 1, "cup"),
   ("feta cheese", 0.5, "cup"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each")],
  "1. Drain and rinse chickpeas.\n2. Dice cucumber and tomato.\n3. Combine all ingredients with olive oil and lemon juice.\n4. Toss and serve.",
  ["vegetarian", "dairy"])

r("Shrimp Scampi", "Mediterranean", 18,
  [("shrimp", 1, "lb"), ("spaghetti", 8, "oz"), ("garlic", 3, "clove"),
   ("olive oil", 3, "tbsp"), ("lemon", 1, "each"), ("parsley", 0.25, "cup")],
  "1. Cook pasta, drain.\n2. Saute garlic in olive oil, add shrimp until pink.\n3. Toss with pasta, lemon juice, parsley.",
  ["shrimp", "shellfish", "gluten"])

r("Falafel Bowls", "Mediterranean", 25,
  [("falafel mix", 10, "oz"), ("rice", 2, "cup"), ("cucumber", 1, "cup"),
   ("tomato", 1, "cup"), ("hummus", 0.5, "cup"), ("lemon", 1, "each")],
  "1. Prepare falafel per package, pan-fry or bake.\n2. Cook rice.\n3. Build bowls with rice, falafel, vegetables, hummus, lemon.",
  ["vegetarian", "gluten"])

r("Greek Salad with Grilled Chicken", "Mediterranean", 20,
  [("chicken breast", 1, "lb"), ("cucumber", 1, "cup"), ("tomato", 1, "cup"),
   ("feta cheese", 0.5, "cup"), ("olives", 0.33, "cup"), ("olive oil", 2, "tbsp")],
  "1. Season and grill chicken, slice.\n2. Combine cucumber, tomato, feta, olives.\n3. Top salad with chicken, drizzle olive oil.",
  ["chicken", "dairy"])

r("Lemon Herb Baked Tilapia", "Mediterranean", 20,
  [("tilapia fillet", 1, "lb"), ("lemon", 1, "each"), ("olive oil", 2, "tbsp"),
   ("oregano", 1, "tsp"), ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Place tilapia on sheet pan, drizzle oil and lemon, season with oregano.\n2. Bake at 400F for 12-15 min.\n3. Steam green beans.\n4. Serve fish over rice with beans.",
  ["fish"])

r("Mediterranean Turkey Meatballs", "Mediterranean", 25,
  [("ground turkey", 1, "lb"), ("feta cheese", 0.5, "cup"), ("oregano", 1, "tsp"),
   ("garlic", 2, "clove"), ("rice", 2, "cup"), ("tomato sauce", 1, "cup")],
  "1. Mix turkey, feta, oregano, garlic; form meatballs.\n2. Pan-sear meatballs until browned.\n3. Add tomato sauce, simmer 10 min.\n4. Serve over rice.",
  ["dairy"])

r("Hummus and Veggie Wrap", "Mediterranean", 10,
  [("hummus", 1, "cup"), ("tortillas", 4, "each"), ("cucumber", 1, "cup"),
   ("tomato", 1, "cup"), ("lettuce", 1, "cup"), ("feta cheese", 0.5, "cup")],
  "1. Spread hummus on tortillas.\n2. Layer vegetables and feta.\n3. Roll tightly and slice in half.",
  ["vegetarian", "dairy", "gluten"])

r("Greek Lemon Chicken and Rice", "Mediterranean", 28,
  [("chicken thighs", 1, "lb"), ("rice", 2, "cup"), ("lemon", 1, "each"),
   ("chicken broth", 2, "cup"), ("garlic", 2, "clove"), ("oregano", 1, "tsp")],
  "1. Sear chicken thighs until browned.\n2. Add rice, broth, lemon, garlic, oregano to pot.\n3. Cover and simmer 18-20 min until rice is tender.",
  ["chicken"])

r("Mediterranean Tuna Salad", "Mediterranean", 10,
  [("canned tuna", 10, "oz"), ("chickpeas", 15, "oz"), ("cucumber", 1, "cup"),
   ("tomato", 1, "cup"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each")],
  "1. Drain tuna and chickpeas.\n2. Dice cucumber and tomato.\n3. Combine everything with olive oil and lemon juice.",
  ["fish"])

r("Spanakopita-Style Spinach Bake", "Mediterranean", 28,
  [("spinach", 4, "cup"), ("feta cheese", 1, "cup"), ("egg", 2, "each"),
   ("phyllo dough", 8, "sheet"), ("olive oil", 2, "tbsp")],
  "1. Wilt spinach, mix with feta and egg.\n2. Layer phyllo with olive oil brushed between sheets.\n3. Spread filling, fold phyllo over.\n4. Bake at 375F for 18-20 min.",
  ["vegetarian", "dairy", "gluten"])

r("Greek Chicken Pita Sandwiches", "Mediterranean", 20,
  [("chicken breast", 1, "lb"), ("pita bread", 4, "each"), ("tzatziki", 0.5, "cup"),
   ("tomato", 1, "cup"), ("lettuce", 1, "cup"), ("lemon", 1, "each")],
  "1. Season and cook chicken, slice.\n2. Warm pita.\n3. Fill pita with chicken, tzatziki, tomato, lettuce.\n4. Squeeze lemon over top.",
  ["chicken", "dairy", "gluten"])

r("Mediterranean Baked Salmon", "Mediterranean", 20,
  [("salmon fillet", 1, "lb"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each"),
   ("olives", 0.33, "cup"), ("tomato", 1, "cup"), ("rice", 2, "cup")],
  "1. Place salmon on sheet pan with olives and tomato.\n2. Drizzle olive oil and lemon.\n3. Bake at 400F for 12-15 min.\n4. Serve over rice.",
  ["fish"])

r("Couscous with Chickpeas and Vegetables", "Mediterranean", 18,
  [("couscous", 1.5, "cup"), ("chickpeas", 15, "oz"), ("zucchini", 1, "cup"),
   ("tomato", 1, "cup"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each")],
  "1. Prepare couscous per package.\n2. Saute zucchini and tomato in olive oil.\n3. Combine with couscous and chickpeas.\n4. Finish with lemon juice.",
  ["vegetarian", "gluten"])

r("Greek Shrimp and Orzo", "Mediterranean", 22,
  [("shrimp", 1, "lb"), ("orzo", 1.5, "cup"), ("tomato", 1, "cup"),
   ("feta cheese", 0.5, "cup"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each")],
  "1. Cook orzo per package, drain.\n2. Saute shrimp until pink.\n3. Toss orzo with shrimp, tomato, feta, olive oil, lemon.",
  ["shrimp", "shellfish", "dairy", "gluten"])

r("Stuffed Bell Peppers (Mediterranean)", "Mediterranean", 28,
  [("bell pepper", 4, "each"), ("ground turkey", 1, "lb"), ("rice", 1, "cup"),
   ("feta cheese", 0.5, "cup"), ("tomato sauce", 1, "cup"), ("oregano", 1, "tsp")],
  "1. Halve peppers and remove seeds.\n2. Brown turkey, mix with rice, tomato sauce, oregano.\n3. Stuff peppers, top with feta.\n4. Bake at 375F for 20 min.",
  ["dairy"])

r("Mediterranean Veggie Skewers with Hummus", "Mediterranean", 20,
  [("zucchini", 1, "cup"), ("bell pepper", 1, "cup"), ("cherry tomato", 1, "cup"),
   ("olive oil", 2, "tbsp"), ("hummus", 1, "cup"), ("pita bread", 4, "each")],
  "1. Thread vegetables onto skewers.\n2. Brush with olive oil, grill or pan-cook until tender.\n3. Serve with hummus and warm pita.",
  ["vegetarian", "gluten"])

r("Chicken Shawarma Bowls", "Mediterranean", 25,
  [("chicken thighs", 1, "lb"), ("cumin", 1, "tsp"), ("garlic", 2, "clove"),
   ("rice", 2, "cup"), ("cucumber", 1, "cup"), ("tzatziki", 0.5, "cup")],
  "1. Season chicken with cumin and garlic, pan-sear until cooked.\n2. Slice chicken.\n3. Cook rice.\n4. Build bowls with rice, chicken, cucumber, tzatziki.",
  ["chicken", "dairy"])

r("White Bean and Spinach Stew", "Mediterranean", 22,
  [("white beans", 15, "oz"), ("spinach", 3, "cup"), ("tomato", 1, "cup"),
   ("garlic", 2, "clove"), ("olive oil", 2, "tbsp"), ("vegetable broth", 2, "cup")],
  "1. Saute garlic in olive oil.\n2. Add beans, tomato, broth, simmer 10 min.\n3. Stir in spinach until wilted.",
  ["vegetarian"])

r("Greek Baked Cod", "Mediterranean", 20,
  [("cod fillet", 1, "lb"), ("olive oil", 2, "tbsp"), ("lemon", 1, "each"),
   ("tomato", 1, "cup"), ("olives", 0.33, "cup"), ("rice", 2, "cup")],
  "1. Place cod on sheet pan with tomato and olives.\n2. Drizzle olive oil and lemon.\n3. Bake at 400F for 12-15 min.\n4. Serve over rice.",
  ["fish"])

r("Mediterranean Pasta Salad", "Mediterranean", 15,
  [("pasta", 8, "oz"), ("cherry tomato", 1, "cup"), ("cucumber", 1, "cup"),
   ("feta cheese", 0.5, "cup"), ("olives", 0.33, "cup"), ("olive oil", 3, "tbsp")],
  "1. Cook pasta, drain and cool slightly.\n2. Combine with tomato, cucumber, feta, olives.\n3. Toss with olive oil.",
  ["vegetarian", "dairy", "gluten"])

r("Lemon Garlic Chicken Thighs", "Mediterranean", 25,
  [("chicken thighs", 1, "lb"), ("lemon", 1, "each"), ("garlic", 3, "clove"),
   ("olive oil", 2, "tbsp"), ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Sear chicken thighs skin-side down until golden.\n2. Add garlic and lemon, finish cooking through.\n3. Steam green beans.\n4. Serve over rice with beans.",
  ["chicken"])

r("Chickpea and Spinach Curry (Mediterranean Style)", "Mediterranean", 22,
  [("chickpeas", 15, "oz"), ("spinach", 3, "cup"), ("tomato", 1, "cup"),
   ("garlic", 2, "clove"), ("olive oil", 2, "tbsp"), ("rice", 2, "cup")],
  "1. Saute garlic in olive oil.\n2. Add chickpeas and tomato, simmer 8 min.\n3. Stir in spinach until wilted.\n4. Serve over rice.",
  ["vegetarian"])

r("Greek Turkey Burgers", "Mediterranean", 20,
  [("ground turkey", 1, "lb"), ("feta cheese", 0.5, "cup"), ("oregano", 1, "tsp"),
   ("pita bread", 4, "each"), ("tzatziki", 0.5, "cup"), ("tomato", 1, "cup")],
  "1. Mix turkey, feta, oregano; form patties.\n2. Pan-sear patties 5-6 min per side.\n3. Serve in pita with tzatziki and tomato.",
  ["dairy", "gluten"])

# ---------------- AMERICAN (25) ----------------

r("Baked Chicken Tenders", "American", 25,
  [("chicken breast", 1, "lb"), ("breadcrumbs", 1, "cup"), ("egg", 2, "each"),
   ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Slice chicken into strips.\n2. Dip in egg, coat in breadcrumbs.\n3. Bake at 425F for 15-18 min.\n4. Serve with rice and green beans.",
  ["chicken", "gluten"])

r("Turkey Burgers", "American", 18,
  [("ground turkey", 1, "lb"), ("burger buns", 4, "each"), ("lettuce", 1, "cup"),
   ("tomato", 1, "cup"), ("cheddar cheese", 4, "slice")],
  "1. Form turkey into patties, season.\n2. Pan-sear or grill 5-6 min per side.\n3. Assemble burgers with buns, lettuce, tomato, cheese.",
  ["dairy", "gluten"])

r("Baked BBQ Chicken", "American", 28,
  [("chicken thighs", 1, "lb"), ("bbq sauce", 0.5, "cup"), ("rice", 2, "cup"),
   ("corn", 1, "cup")],
  "1. Place chicken on sheet pan, brush with bbq sauce.\n2. Bake at 400F for 22-25 min, basting halfway.\n3. Serve with rice and corn.",
  ["chicken"])

r("Sheet Pan Sausage and Veggies", "American", 25,
  [("chicken sausage", 1, "lb"), ("bell pepper", 2, "cup"), ("zucchini", 1, "cup"),
   ("olive oil", 2, "tbsp"), ("potato", 2, "cup")],
  "1. Slice sausage and vegetables, toss with oil on sheet pan.\n2. Roast at 425F for 20-22 min, stirring halfway.",
  ["pork"])

r("Classic Beef Chili", "American", 28,
  [("ground beef", 1, "lb"), ("kidney beans", 15, "oz"), ("tomato", 2, "cup"),
   ("onion", 0.5, "cup"), ("chili powder", 1, "tbsp"), ("cheddar cheese", 0.5, "cup")],
  "1. Brown beef with onion.\n2. Add beans, tomato, chili powder, simmer 15 min.\n3. Top with cheese.",
  ["beef", "dairy"])

r("Turkey Meatloaf Muffins", "American", 28,
  [("ground turkey", 1, "lb"), ("breadcrumbs", 0.5, "cup"), ("egg", 1, "each"),
   ("ketchup", 3, "tbsp"), ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Mix turkey, breadcrumbs, egg, half the ketchup. Form into muffin tin cups.\n2. Top with remaining ketchup.\n3. Bake at 375F for 18-20 min.\n4. Serve with rice and green beans.",
  ["gluten"])

r("Grilled Chicken Caesar Salad", "American", 18,
  [("chicken breast", 1, "lb"), ("romaine lettuce", 4, "cup"), ("parmesan cheese", 0.5, "cup"),
   ("caesar dressing", 0.33, "cup"), ("croutons", 1, "cup")],
  "1. Season and grill chicken, slice.\n2. Toss lettuce with dressing and parmesan.\n3. Top with chicken and croutons.",
  ["chicken", "dairy", "gluten"])

r("Baked Salmon with Roasted Potatoes", "American", 28,
  [("salmon fillet", 1, "lb"), ("potato", 2, "cup"), ("olive oil", 2, "tbsp"),
   ("lemon", 1, "each"), ("green beans", 2, "cup")],
  "1. Toss potatoes with oil, roast at 425F for 15 min.\n2. Add salmon and green beans to pan, roast 10-12 min more.\n3. Finish with lemon.",
  ["fish"])

r("Sloppy Joes", "American", 20,
  [("ground beef", 1, "lb"), ("tomato sauce", 1, "cup"), ("ketchup", 2, "tbsp"),
   ("burger buns", 4, "each"), ("onion", 0.5, "cup")],
  "1. Brown beef with onion.\n2. Stir in tomato sauce and ketchup, simmer 10 min.\n3. Serve on buns.",
  ["beef", "gluten"])

r("Chicken Noodle Soup", "American", 25,
  [("chicken breast", 1, "lb"), ("egg noodles", 2, "cup"), ("carrot", 1, "cup"),
   ("celery", 1, "cup"), ("chicken broth", 6, "cup")],
  "1. Poach chicken in broth until cooked, shred.\n2. Add carrot, celery, simmer 8 min.\n3. Add noodles, cook until tender.",
  ["chicken", "gluten"])

r("BBQ Pulled Pork Sandwiches (Quick)", "American", 25,
  [("pork tenderloin", 1, "lb"), ("bbq sauce", 0.75, "cup"), ("burger buns", 4, "each"),
   ("cabbage", 1, "cup"), ("mayonnaise", 2, "tbsp")],
  "1. Slice pork thin, sear until cooked through.\n2. Shred with forks, toss with bbq sauce.\n3. Toss cabbage with mayo for slaw.\n4. Serve pork on buns topped with slaw.",
  ["pork", "gluten"])

r("Baked Mac and Cheese with Broccoli", "American", 25,
  [("macaroni", 2, "cup"), ("cheddar cheese", 2, "cup"), ("milk", 1, "cup"),
   ("broccoli", 2, "cup"), ("butter", 2, "tbsp")],
  "1. Cook macaroni, drain.\n2. Melt butter, whisk in milk and cheese to make sauce.\n3. Steam broccoli.\n4. Combine pasta, sauce, broccoli; bake at 375F for 10 min if desired.",
  ["vegetarian", "dairy", "gluten"])

r("Honey Mustard Chicken", "American", 25,
  [("chicken breast", 1, "lb"), ("honey", 2, "tbsp"), ("mustard", 2, "tbsp"),
   ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Whisk honey and mustard.\n2. Sear chicken, brush with honey mustard, finish cooking through.\n3. Steam green beans.\n4. Serve over rice.",
  ["chicken"])

r("Turkey Chili", "American", 25,
  [("ground turkey", 1, "lb"), ("kidney beans", 15, "oz"), ("tomato", 2, "cup"),
   ("onion", 0.5, "cup"), ("chili powder", 1, "tbsp"), ("cheddar cheese", 0.5, "cup")],
  "1. Brown turkey with onion.\n2. Add beans, tomato, chili powder, simmer 15 min.\n3. Top with cheese.",
  ["dairy"])

r("Pan-Seared Pork Chops with Apples", "American", 22,
  [("pork chops", 1, "lb"), ("apple", 2, "each"), ("butter", 2, "tbsp"),
   ("rice", 2, "cup"), ("green beans", 2, "cup")],
  "1. Sear pork chops 4-5 min per side, set aside.\n2. Saute sliced apples in butter until soft.\n3. Steam green beans.\n4. Serve chops topped with apples, rice on side.",
  ["pork", "dairy"])

r("Beef and Vegetable Stir-Fry (American Style)", "American", 20,
  [("flank steak", 1, "lb"), ("broccoli", 2, "cup"), ("carrot", 1, "cup"),
   ("soy sauce", 2, "tbsp"), ("rice", 2, "cup")],
  "1. Slice steak thin, sear until browned.\n2. Add vegetables, stir-fry 5 min.\n3. Add soy sauce, toss.\n4. Serve over rice.",
  ["beef", "soy", "gluten"])

r("Classic Hamburgers", "American", 18,
  [("ground beef", 1, "lb"), ("burger buns", 4, "each"), ("cheddar cheese", 4, "slice"),
   ("lettuce", 1, "cup"), ("tomato", 1, "cup")],
  "1. Form beef into patties, season.\n2. Grill or pan-sear 4-5 min per side.\n3. Assemble with buns, cheese, lettuce, tomato.",
  ["beef", "dairy", "gluten"])

r("Lemon Pepper Baked Chicken", "American", 28,
  [("chicken thighs", 1, "lb"), ("lemon", 1, "each"), ("black pepper", 1, "tsp"),
   ("potato", 2, "cup"), ("green beans", 2, "cup")],
  "1. Toss potatoes with oil, start roasting at 425F for 10 min.\n2. Add chicken seasoned with lemon and pepper, roast 18-20 min more.\n3. Steam green beans, serve alongside.",
  ["chicken"])

r("Shrimp Boil Skillet", "American", 20,
  [("shrimp", 1, "lb"), ("potato", 2, "cup"), ("corn", 1, "cup"),
   ("butter", 2, "tbsp"), ("garlic", 2, "clove")],
  "1. Boil potatoes until just tender, about 10 min.\n2. Add corn and shrimp, cook 5 min more.\n3. Toss with melted butter and garlic.",
  ["shrimp", "shellfish", "dairy"])

r("Baked Ziti with Turkey", "American", 28,
  [("ground turkey", 1, "lb"), ("ziti pasta", 2, "cup"), ("tomato sauce", 2, "cup"),
   ("mozzarella cheese", 1.5, "cup"), ("parmesan cheese", 0.5, "cup")],
  "1. Cook pasta, drain.\n2. Brown turkey, add tomato sauce.\n3. Combine pasta and sauce, top with cheeses.\n4. Bake at 400F for 12-15 min.",
  ["dairy", "gluten"])

r("Cobb Salad", "American", 15,
  [("chicken breast", 1, "lb"), ("romaine lettuce", 4, "cup"), ("egg", 2, "each"),
   ("bacon", 4, "slice"), ("cheddar cheese", 0.5, "cup"), ("tomato", 1, "cup")],
  "1. Cook and slice chicken.\n2. Hard-boil and chop eggs; cook and crumble bacon.\n3. Arrange lettuce with chicken, egg, bacon, cheese, tomato in rows.",
  ["chicken", "pork", "dairy"])

r("Garlic Butter Steak Bites with Potatoes", "American", 22,
  [("sirloin steak", 1, "lb"), ("potato", 2, "cup"), ("butter", 3, "tbsp"),
   ("garlic", 3, "clove"), ("green beans", 2, "cup")],
  "1. Boil or microwave potatoes until just tender, cube.\n2. Sear steak bites in butter and garlic until browned.\n3. Add potatoes, toss to coat.\n4. Steam green beans, serve alongside.",
  ["beef", "dairy"])

r("Chicken and Rice Casserole", "American", 28,
  [("chicken breast", 1, "lb"), ("rice", 2, "cup"), ("chicken broth", 2, "cup"),
   ("cheddar cheese", 1, "cup"), ("frozen peas and carrots", 1, "cup")],
  "1. Cube chicken, brown in pot.\n2. Add rice, broth, vegetables; cover and simmer 18 min.\n3. Stir in cheese until melted.",
  ["chicken", "dairy"])

r("Turkey and Veggie Skewers", "American", 20,
  [("ground turkey", 1, "lb"), ("zucchini", 1, "cup"), ("bell pepper", 1, "cup"),
   ("olive oil", 2, "tbsp"), ("rice", 2, "cup")],
  "1. Form turkey into small meatballs.\n2. Thread meatballs and vegetables onto skewers, brush with oil.\n3. Grill or pan-cook until turkey is cooked through.\n4. Serve over rice.",
  [])

r("Sheet Pan Chicken Fajita Bake", "American", 25,
  [("chicken breast", 1, "lb"), ("bell pepper", 2, "cup"), ("onion", 1, "cup"),
   ("taco seasoning", 2, "tbsp"), ("rice", 2, "cup")],
  "1. Slice chicken and vegetables, toss with seasoning and oil on sheet pan.\n2. Roast at 425F for 18-20 min.\n3. Serve over rice.",
  ["chicken"])
