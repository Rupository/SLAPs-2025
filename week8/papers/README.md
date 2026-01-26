### Research Survey and Positioning

#### CAV03.pdf
1. Problem Statement: What problem does the paper solve?
    - Allows us to find linear invariants with linear update rules
    - Some clever translation is done to write the problem in the form of different linear/non linear constraint solving tools
    - Solving the latter is less non-trivial for smaller systems, thus aiding in finding coefficients to linear invariants easily.

2. Approach: What is the technical approach?
    - Farkas' Lemma!
        - Crux of the whole approach
        - It posits that a universally quanitfied statement on the conjunction of linear inequalities can be converted to an existentially quantified set of linear combinations over the coefficients of the inequalities.
        - Universal quantification: ow. Existential quantification: yippeee
    - Translating the linear invariant, a polynomial inequality, is done via a transition system, with the current and next states. These are all modeled appropriately, Farkas-ified, and then solved.

3. Contributions: What are the key contributions?
    - Novel and robust method of generting invariants without worrying about "widening" for termination, unlike abstract interpretation
    - The method does not need to work iteratively towards a fixed point - just existential checking
    - The method will be streghthened by developements in Non-Linear Constraint Solving
    
4. Limitations: What are the limitations?
    - Produces non linear constraints - works for small systems, explodes in complexity for larger systems.
    - Non-linear ==> multiplication of (existential) constraint variables, multiplication is undecidable!

5. Relevance: How does it relate to your work?
    - This paper is kind of my whole project summarized
    - Non-Linear Constraint Solving did get better - Z3 happened!
    - After translating to Farkas' lemma appropriately, I used their exact method.
    - I ended up reinventing one of their tips and realised it later!

    > Another heuristic, especially effective when the result of the elimination is too large to be factorized or simplified, is to set some of the coefficients to zero, in effect restricting the target invariants to those involving only a subset of the variables of the program. Furthermore, since any two-dimensional cone is finitely generated, setting sufficiently many variables to zero always yields a polyhedral cone.

#### CAV08.pdf
1. Problem Statement: What problem does the paper solve?
    - Application of Farkas' Lemma based setup as described previously to **verify** hybrid systems
    - States the "synthesis" oriented approach of CAV03 as a setup for verification and achieves key results

2. Approach: What is the technical approach?
    - Farkas' Lemma, again. A hybrid system has a bunch of universally quantified states and preexisting constraints, representable as inequalities. To check if a safety constraint is held, apply Farkas and see if it arrives at that something within the bounds of that safety constraint. Or, check if it's unsafe when by solving Farkas' and arriving at an unsafe state.
    - Combined with SMT solving for arriving at constraints, made more efficient via converting to more efficient satisfiability setups

3. Contributions: What are the key contributions?
    - Strong and robust application of of Farkas setup
    - Works in the continuous domain, utilises lie derivatives (idk what that means but it feels lin-al + calculusy) for smooth and effective "updates"
    - Conversion of SAT to bit-SAT
    - Ideas for various other applications of this method on more problems.
    
4. Limitations: What are the limitations?
    - Larger hybrid systems are likely to fail given aforementioned issues with this setup
    - This is a problem, as hybrid systems often grow quickly in complexity
    - The smoothness of continuity and lie derivatives are also hard to come by, many systems are discrete - such as incremental loop invariants

5. Relevance: How does it relate to your work?
    - The authors expect invariant synthesis to be one of the key ways this method is applied. This is what we've taken up!

    > Our constraint-based technique for verification can be used for solving in-stances of the synthesis problem as well. The technique uniformly treats the en-tities of the verification condition, which includes both the inductive invariants and the description of the system. It does not matter whether the invariants are unknown or parts of the system are unknown or both of them are unknown. As long as there is sufficient information in the system description, the constraint-based approach can potentially find a solution for the unknown quantities.

