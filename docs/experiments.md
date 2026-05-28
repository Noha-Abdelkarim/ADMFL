# docs/experiments.md

# ADMFL Experimental Guide

## Supported Experiments

ADMFL supports:

- Federated Learning experiments
- attack simulations
- trust convergence evaluation
- SDN mitigation experiments
- P4 filtering evaluation

---

# Experiment 1 — Federated Learning

Run:

```bash
python tafl/fl_server.py
```

Evaluates:
- FL convergence
- aggregation performance
- trust-weighted aggregation

---

# Experiment 2 — DDoS Attack

Run:

```bash
python attacks/ddos_attack.py
```

Evaluates:
- detection latency
- mitigation effectiveness
- throughput stability

---

# Experiment 3 — Spoofing Attack

Run:

```bash
python attacks/spoofing_attack.py
```

Evaluates:
- trust degradation
- spoofing detection rate

---

# Experiment 4 — Poisoning Attack

Run:

```bash
python attacks/poisoning_attack.py
```

Evaluates:
- FL robustness
- aggregation resilience

---

# Experiment 5 — Swarm Attack

Run:

```bash
python attacks/swarm_attack.py
```

Evaluates:
- orchestration scalability
- routing adaptation

---

# Evaluation Metrics

The framework computes:

- accuracy
- precision
- recall
- F1-score
- throughput
- packet loss
- detection latency

---

# Visualization

Generate plots using:

```bash
python visualization/plot_metrics.py
```

---

# Results

Experimental outputs are saved in:

```text
results/
```