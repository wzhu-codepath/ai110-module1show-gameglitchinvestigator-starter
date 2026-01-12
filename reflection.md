# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  1. It looked like a number guessing game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. The hint to go higher or lower is severely inaccurate. For example if the secret code was 65, and I put 50, the hint will tell me to go lower. If my input as -50 for example it will also tell me to go lower, which isn't possible as that would be out of bounds (1-100) and I should not be going lower.
  2. The button for "New Game" does not work. In order to restart you would need to refresh the page.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  1. Copilot
- Give one example of an AI suggestion you accepted and why.
  1. Accepted the suggestion to fix the typos in the outputs as it caught one of the crucial erros affecting the game.
- Give one example of an AI suggestion you changed or rejected and why.
  1. Copilot removed the exception handling in which the test cases was depending on that. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  1. Ran test cases plus tried it out my self. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  1. Going lower than the threshold to see if it tells me to go higher. This was done with both pytest and manually.
- Did AI help you design or understand any tests? How?
  1. It helped me write some of the test cases such as returning the Tuple, which I would never would have thought of without AI. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  1. The secret number was randomized each time. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  1. It is reran everytime an interaction is logged whether it be inputting a new number or changing the difficulty of the came. 
- What change did you make that finally gave the game a stable secret number?
  1. I didn't make any changes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  1. Never trust AI, verify everything it provides you. Question it if you are unsure. 
- What is one thing you would do differently next time you work with AI on a coding task?
  1. Not relying on AI to write code for everything without prior review. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  1. While AI is great at generating code, it still reviews a human to review whether the work is actually good.
   
---

## 6. Reflection Questions
- Which Copilot mode (e.g., Agent, Edit, or Inline Chat) was most effective for refactoring your code?
  1. Agent was most effective as I was able to interact with it. I also used Agent the entire time
- How did providing context (like using #codebase or #file) change the quality of the AI's suggestions?
  1. It provided the AI with reasoning to go through everything rather than a single file
- What did you learn about "session hygiene"? Did keeping your chat sessions separate help you stay organized?
  1. Yes. AI could go back to previous memory which can be good and bad. Bad if the previous context was bad. 