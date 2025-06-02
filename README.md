# course-tools
Nástroje pre simuláciu ransomvérových útokov a generovanie tréningových dát na účely kybernetickej bezpečnosti.

## O projekte

Tento projekt poskytuje jednoduché skripty a utility na:
- simuláciu ransomvérového útoku nad súbormi (šifrovanie / dešifrovanie),
- generovanie .pcap súborov so sieťovou prevádzkou pre tréning a testovanie,
- podporu praktických cvičení v oblasti IT bezpečnosti.

## Štruktúra projektu

- `ransomware.py` – Simulácia šifrovania súborov (ransomware).
- `decrypt.py` – Dešifrovanie súborov šifrovaných pomocou ransomware.py.
- `training_pcap_generator.py` – Generátor ukážkovej sieťovej komunikácie do .pcap súborov.
- `materials/` – Ukážkové materiály a vzorové dáta.

## Požiadavky

- Python 3.8+
- Balíčky:  
  - `scapy`  
  - `cryptography`  
  - `argparse` (štandardná knižnica)

Všetky závislosti nainštaluješ pomocou:

```bash
pip install -r requirements.txt
