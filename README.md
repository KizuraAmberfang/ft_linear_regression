# ft_linear_regression

## Denormalizzazione della retta

Una volta ottenuta la retta normalizzata dobbiamo occuparci di ottenere la retta per i dati reali. Per farlo ho deciso di ottenere la retta interpolante il punto di minimo (A) e di massimo dei dati (B). 

<img src="https://render.githubusercontent.com/render/math?math=x = min(X)">

Usando la formula di normalizzazione dei dati otteniamo che 

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{min(X) - min(X)}{max(X) - min(X)} = 0 ">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \overline{\theta_1}\overline{x} %2B \overline{\theta_0} = \overline{\theta_0} ">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \frac{y - min(Y)}{max(Y) - min(Y)}">

<img src="https://render.githubusercontent.com/render/math?math=\overline{\theta_0} = \frac{y - min(Y)}{max(Y) - min(Y)}">

<img src="https://render.githubusercontent.com/render/math?math=\overline{\theta_0}(max(Y) - min(Y)) = y - min(Y)">

<img src="https://render.githubusercontent.com/render/math?math=y = \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y)">

<img src="https://render.githubusercontent.com/render/math?math=A = (min(X), \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y))">

Stessa cosa la applichiamo per trovare il punto B:

<img src="https://render.githubusercontent.com/render/math?math=x = max(X)">

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{max(X) - min(X)}{max(X) - min(X)} = 1 ">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \overline{\theta_1}\overline{x} %2B \overline{\theta_0} = \overline{\theta_1} %2B \overline{\theta_0} ">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \frac{y - min(Y)}{max(Y) - min(Y)}">

<img src="https://render.githubusercontent.com/render/math?math=\overline{\theta_0} %2B \overline{\theta_1} = \frac{y - min(Y)}{max(Y) - min(Y)}">

<img src="https://render.githubusercontent.com/render/math?math=(\overline{\theta_0} %2B \overline{\theta_1})(max(Y) - min(Y)) = y - min(Y)">

<img src="https://render.githubusercontent.com/render/math?math=y = (\overline{\theta_0} %2B \overline{\theta_1})(max(Y) - min(Y)) %2B min(Y)">

<img src="https://render.githubusercontent.com/render/math?math=B = (max(X), (\overline{\theta_0} %2B \overline{\theta_1})(max(Y) - min(Y)) %2B min(Y)">

A questo punto otteniamo la retta passante per i due punti:

<img src="https://render.githubusercontent.com/render/math?math=\frac{y - y_A}{y_B - y_A} = \frac{x - x_A}{x_B - x_A}">

