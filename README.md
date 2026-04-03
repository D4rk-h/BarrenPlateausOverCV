# Study of CV-VQE over Bose-Hubbard model from a Wigner-Weyl perspective

A framework designed to replicate the numerical analysis performed by Stornati et al. in the paper [Stornati.pdf](Stornati.pdf). 

This work presents a **numerical replication** rather than a purely mathematical one. The mathematical framework underlying this replication follows the **Wigner–Weyl formalism**. We consider an analytical function representing the **expectation value of a Hamiltonian** **H**, expressed as:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\color{white}\langle%20H%20\rangle%20=%20\frac{1}{K}\int%20H(\xi)\,W_{\text{ansatz}}(\xi)\,d^{2N}\xi" 
       alt="⟨H⟩ = (1/K) ∫ H(ξ) W_ansatz(ξ) d²ᴺξ">
</p>

where  
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\color{white}W_{\text{ansatz}}(\xi)%20=%20P^{(2L)}(\xi)\,W_G(\xi)" 
       alt="W_ansatz(ξ) = P^(2L)(ξ) W_G(ξ)">
</p>

The term **P⁽²ᴸ⁾(ξ)** denotes a polynomial constructed through the **Moyal product** of *L* ladder operations, while **W_G(ξ)** represents a **Gaussian Wigner function** generated solely via **interferometric and squeezing operations**.
