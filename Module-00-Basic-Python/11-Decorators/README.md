✨ The Art of Decorators: Adding Superpowers to Your Functions
Welcome to a deep dive into one of Python's most elegant features: Decorators. Think of them as a way to add superpowers to your functions without changing their internal code.

🤔 What is a Decorator? The Gift-Wrapping Analogy
Imagine you have a simple function. This function is a gift—it does one thing well.

def say_hello():
    return "Hello!"

Now, what if you want to add something extra to this function every time it's called? Maybe you want to log when it runs, or time how long it takes. You could modify the function directly, but that gets messy.

Instead, you can "wrap" it in a decorator.

A decorator is like gift-wrapping your function. The gift inside ("Hello!") remains the same, but the decorator adds a beautiful new layer on the outside (e.g., logging, timing, etc.).

🚀 How It Works: A Simple Example
Let's create a decorator that logs when a function is about to run and when it has finished.

# This is our decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"🎁 Wrapping '{func.__name__}'... about to run!")
        result = func(*args, **kwargs)
        print(f"✨ Unwrapped '{func.__name__}'... it's done!")
        return result
    return wrapper

# Now, let's apply our decorator to a function
@log_execution
def calculate_sum(a, b):
    print("   Inside the function: Calculating...")
    return a + b

# Let's run our decorated function
final_sum = calculate_sum(10, 5)
print(f"The final result is: {final_sum}")

What happens when you run this?

The @log_execution syntax is Python's special sugar for applying the decorator.

When you call calculate_sum(10, 5), you are actually calling the wrapper function inside the decorator.

The wrapper prints the "before" message, runs the original calculate_sum function, prints the "after" message, and then returns the result.

Expected Output:

🎁 Wrapping 'calculate_sum'... about to run!
   Inside the function: Calculating...
✨ Unwrapped 'calculate_sum'... it's done!
The final result is: 15

✅ Why Use Decorators?
Decorators are used everywhere in professional Python code for tasks that need to be repeated across many functions. This is known as cross-cutting concerns.

Logging: Add logging statements before and after function calls.

Timing: Time how long a function takes to execute.

Authentication: Check if a user is logged in before allowing them to run a function.

Caching: Store the results of a function so you don't have to compute it again.

Tool Registration: In LangChain and LangGraph, the @tool decorator automatically registers a normal Python function as a tool that an AI agent can use.

By using decorators, you keep your core logic clean and separate from these repeated tasks, making your code much easier to read and maintain.