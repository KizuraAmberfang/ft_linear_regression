# ft_linear_regression

## Denormalizzazione della retta

Una volta ottenuta la retta normalizzata dobbiamo occuparci di ottenere la retta per i dati reali. Per farlo ho deciso di ottenere la retta interpolante il punto di minimo (A) e di massimo dei dati (B). 

<img src="https://render.githubusercontent.com/render/math?math=x = min(X)">

Usando la formula di normalizzazione dei dati otteniamo che 

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{min(X) - min(X)}{max(X) - min(X)} = 0 ">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \theta_1\overline{x} %2B \theta_0 = \theta_0 ">

<img src="https://render.githubusercontent.com/render/math?math=A = (0, \theta_0)">
