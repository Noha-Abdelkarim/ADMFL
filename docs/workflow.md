# docs/workflow.md

# ADMFL Workflow

## Step 1 — Network Initialization

The framework initializes:

- UAV nodes
- edge servers
- SDN controller
- P4 switches
- communication links

Main modules:
- network_topology.py
- ryu_controller.py

---

# Step 2 — Telemetry Collection

Each UAV continuously sends:

- packet rate
- latency
- entropy
- throughput
- trust information

Main module:
- telemetry_extractor.py

---

# Step 3 — Anomaly Detection

Collected telemetry is analyzed to detect:

- abnormal traffic
- malicious communication
- poisoned FL updates

Main module:
- anomaly_detector.py

---

# Step 4 — Trust Computation

The trust engine computes dynamic trust scores for UAVs.

Low-trust UAVs are marked as suspicious.

Main module:
- trust_engine.py

---

# Step 5 — Local Federated Training

Each UAV performs:
- local dataset training
- model optimization
- gradient generation

Main modules:
- local_training.py
- fl_client.py

---

# Step 6 — Trust-Aware Aggregation

The FL server:
- collects local updates
- filters malicious clients
- performs trust-weighted aggregation

Main modules:
- fl_server.py
- trust_weighted_fedavg.py

---

# Step 7 — SDN-Based Mitigation

If attacks are detected:

- suspicious UAVs are isolated
- malicious flows are blocked
- routes are dynamically updated

Main modules:
- mitigation_engine.py
- orchestration_engine.py
- routing_manager.py

---

# Step 8 — P4 Data Plane Enforcement

The P4 switch:
- inspects traffic
- applies forwarding rules
- drops suspicious packets

Main module:
- admfl_switch.p4

---

# Step 9 — Attack Simulation

Attack modules generate:
- DDoS traffic
- spoofed packets
- poisoned FL updates
- swarm attacks

Main modules:
- ddos_attack.py
- spoofing_attack.py
- poisoning_attack.py
- swarm_attack.py

---

# Step 10 — Evaluation

The framework computes:
- FL accuracy
- attack detection rate
- mitigation latency
- throughput stability

Main modules:
- metrics.py
- results_analyzer.py
- plot_metrics.py