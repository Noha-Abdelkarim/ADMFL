# docs/architecture.md

# ADMFL Architecture

## Overview

ADMFL is a secure and trust-aware federated learning framework designed for UAV-enabled SD-IoT environments. The framework integrates:

- Federated Learning (FL)
- SDN-based orchestration
- P4 programmable data plane
- Trust management
- Intrusion detection
- Dynamic attack mitigation

The architecture is divided into four major layers:

1. USC Layer
2. IDT Layer
3. TAFL Layer
4. SOAM Layer

---

# 1. USC Layer (UAV Swarm Communication)

The USC layer manages UAV communications and local model training.

## Components

### UAV Client
Handles:
- UAV initialization
- telemetry exchange
- participation in FL rounds

### Communication Manager
Handles:
- UAV-to-UAV communication
- edge communication
- wireless link management

### Local Training
Handles:
- local dataset processing
- local neural network updates
- model optimization

---

# 2. IDT Layer (Intrusion Detection and Trust)

The IDT layer detects attacks and evaluates UAV trustworthiness.

## Components

### Telemetry Extractor
Collects:
- packet statistics
- latency
- entropy
- throughput
- trust indicators

### Anomaly Detector
Detects:
- DDoS attacks
- spoofing attacks
- poisoning attacks

### Trust Engine
Computes:
- dynamic trust scores
- malicious UAV classification

### Security Enforcer
Applies:
- firewall rules
- UAV isolation
- traffic filtering

---

# 3. TAFL Layer (Trust-Aware Federated Learning)

The TAFL layer manages FL aggregation and trust-aware learning.

## Components

### FL Server
Coordinates:
- global model aggregation
- client registration
- FL rounds

### FL Client
Performs:
- local model training
- local update transmission

### Aggregation Manager
Implements:
- FedAvg
- weighted aggregation

### Trust Weighted FedAvg
Performs:
- trust-aware aggregation
- malicious update filtering

---

# 4. SOAM Layer (SDN-Orchestrated Attack Mitigation)

The SOAM layer provides programmable orchestration and mitigation.

## Components

### Ryu Controller
Handles:
- SDN flow management
- network monitoring

### Orchestration Engine
Handles:
- policy orchestration
- mitigation decisions

### Mitigation Engine
Applies:
- packet filtering
- traffic rerouting
- UAV isolation

### Routing Manager
Handles:
- dynamic routing
- congestion-aware routing

---

# P4 Data Plane

The programmable switch layer enables:

- traffic inspection
- suspicious packet marking
- flow-level filtering
- programmable forwarding

---

# Attack Models

ADMFL supports simulation of:

- DDoS attacks
- spoofing attacks
- poisoning attacks
- swarm attacks

---

# Evaluation Metrics

The framework evaluates:

- accuracy
- precision
- recall
- F1-score
- latency
- throughput
- packet loss

---

# Deployment Environment

ADMFL supports:

- Docker deployment
- Mininet integration
- BMv2 P4 switches
- Ryu SDN controller
- Python simulation environment