# Monte-Carlo-Simulation einer Bremer Steuerreform

**Effizienz- und Verteilungswirkungen einer Umschichtung von 
Grunderwerbsteuer und Gewerbesteuer in die Grundsteuer**

---
`mc_tax_reform.pdf` ist die vollständige Analyse (~23 Seiten)  
`mc_tax_reform.ipynb` ist ein Jupyter Notebook mit Python-Code (der online Appendix)



## Zusammenfassung

Diese Analyse untersucht eine aufkommensneutrale Steuerreform in Bremen, 
die 100 Millionen Euro aus der Grunderwerbsteuer und 500 Millionen Euro 
aus der Gewerbesteuer in die Grundsteuer umschichtet. Da die Steuerbasis 
der Grundsteuer erheblich unelastischer ist als die der anderen beiden 
Steuern, sollte diese Umschichtung die ökonomischen Kosten der Bremer 
Steuern – den *deadweight loss* – reduzieren.

Über die genaue Größe dieser Kosten und die Verteilungswirkung der Reform 
besteht erhebliche Unsicherheit. Die Analyse verwendet daher 
Monte-Carlo-Methoden: 100.000 Simulationen, in denen alle relevanten 
Parameter aus empirisch begründeten Wahrscheinlichkeitsverteilungen 
gezogen werden. Hierzu beziehe ich mich auf ökonometrische Ergebnisse 
der Steuerforschung.

**Zentrale Ergebnisse:**
- Effizienzgewinn von durchschnittlich **330 Millionen 
  Euro pro Jahr** (mittlere zwei Drittel der Verteilung: 220–430 Mio.)
- In mindestens **90 % der Simulationen** Nutzen-positiv unter realistischen Annahmen,
in **ca. 97 %** für optimistische Annahmen und in über **65 %** für 
pessimistische Annahmen.
- Langfristig kommen **150–500 Millionen Euro pro Jahr** durch 
  steuerinduziertes Wachstum hinzu
- Die Steuerverschiebung wirkt tendenziell regressiv; im pessimistischen 
  Szenario lässt sich das durch ein begleitendes Umverteilungsprogramm 
  beheben


## Methodik

Die Simulation kombiniert mehrere statistische Methoden:

- **DWL-Schätzung:** Abgeschnittene Normalverteilung (Grundsteuer), 
  $t$-Verteilung per Inversionsmethode (Grunderwerbsteuer) und 
  Dreiecksverteilung (Gewerbesteuer), jeweils aus empirischer Literatur 
  kalibriert
- **Steuerliche Inzidenz:** Stückweise lineare Inzidenzkurven über 
  Einkommensdezile; korrelierte Zufallsvektoren via Gram-Schmidt-Verfahren
- **Wachstumseffekte:** Kalibriert aus meta-analytischen Schätzern 
  (Alinaghi/Reed 2021), modelliert als dauerhafter Niveaueffekt
- **Wohlfahrtsgewichte:** Isoelastische Nutzenfunktionen mit gepoolt 
  geschätztem $\eta$-Parameter sowie begrenzte Gewichte nach Boardman 
  et al., die die Opportunitätskosten direkter Umverteilung abbilden


### Verwendete Bibliotheken
```python
numpy
scipy
pandas
matplotlib
```

## Notebook interaktiv ausführen

Das Notebook kann ohne lokale Installation direkt im Browser ausgeführt 
werden:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RkHlSbcHgnifvECknQH-DhMCXyrqQ85o?usp=sharing)

Parameter können frei verändert und die Simulationen neu ausgeführt 
werden. Mit `num_sim = 10000` dauert jede Zelle etwa 5–10 Sekunden; 
die vollständigen 100.000 Simulationen der Analyse entsprechend länger.