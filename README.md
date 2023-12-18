# Markov Modeling

This folder contains Python scripts implementing Markov chain models for different scenarios. The two exercises explore Markov processes in the context of health status transitions and financial states.

## Exercise 1: Health Status Transition

- **Exercice1.py**: Python script implementing a Markov chain for health status transitions.
  
  - The script defines a transition matrix `A` representing the probabilities of transitioning between health states.
  
  - Functions include:
    - `probabilité_invariante`: Computes the invariant probability of the Markov chain.
    - `état_jour_n`: Calculates the state distribution on the nth day given an initial distribution.
    - `Matrice_puissance_n`: Computes the power of the transition matrix.
    - `adam`: Simulates the Markov chain dynamics.
  
  - Simulation results and calculations are provided for various scenarios, demonstrating the evolution of health states over time.

## Exercise 2: Financial State Transition

- **Exercice2.py**: Python script implementing a Markov chain for financial state transitions.

  - The script defines a transition matrix `A` representing the probabilities of transitioning between financial states.
  
  - Functions include:
    - `Morty_fortune`: Calculates the fortune distribution on the nth day given an initial distribution.
    - `Morty`: Simulates the financial state transitions for Morty.
    - `simulation`: Conducts a single simulation of financial state transitions.
    - `pr`: Conducts multiple simulations and calculates the proportions of each financial state.
    - `Esperance`: Calculates the number of times the simulation converges to a specific state.

  - Simulation results and calculations are provided for different scenarios, showcasing the evolution of Morty's financial states and statistical analyses.

Feel free to explore and modify the scripts to suit your needs or integrate them into your projects. If you have any questions or suggestions, please reach out!

**Note:** Ensure you have NumPy installed (`pip install numpy`) before running the scripts.
