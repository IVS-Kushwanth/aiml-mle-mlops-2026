# Day 2 – Loops & Control Flow

## What I Practiced

- for loop
- while loop
- reverse loops
- range(start, stop, step)
- continue
- break
- Custom step patterns

---

## Key Learnings

### 1 range(start, stop, step)

Loop behavior depends completely on:

- start → where it begins
- stop → where it ends (exclusive)
- step → direction and jump size

Example:
range(10, 0, -3)

Starts at 10  
Moves backward by 3  
Stops before 0  

Output:
10 7 4 1

---

### 2 Why range(10, 0, 3) Prints Nothing

Because:
- Start = 10
- Stop = 0
- Step = +3 (forward)

But 10 < 0 is false.

So Python sees impossible movement → empty range.

Loop logic must match direction.

---

### 3 Why We Use N + 1

range excludes the stop value.

So if we want to include N:

range(-N, N + 1, 5)

Without +1, N will not be printed.

---

### 4 continue

continue does NOT skip the number.

It skips the remaining code inside that iteration and moves to next iteration.

Used for:
- Filtering data
- Skipping invalid conditions
- Ignoring unwanted cases

Example:
Skip even numbers:
if i % 2 == 0:
    continue

---

### 5 break

break completely stops the loop.

Used when:
- Desired value is found
- No need to continue iteration
- Prevent infinite loop

---

### 6 Important Pattern Cases Practiced

1. N to 2 (decreasing by 3)
2. -N to N (increasing by 5)
3. M to -N (decreasing by P)

Used abs() to ensure step is positive before applying negative direction.

---

## Mental Model I Built

Loop execution depends on:

- Direction must match step
- Stop value is exclusive
- Step sign determines movement
- Wrong direction = empty loop

---

## Self Audit

 I can predict loop output without running  
 I understand why empty loops happen  
 I understand continue vs break  
 I understand inclusive vs exclusive range  

If I hesitate → revise again.
