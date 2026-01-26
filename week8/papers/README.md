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
