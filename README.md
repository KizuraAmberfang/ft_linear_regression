# ft_linear_regression

[![jaeskim's 42Project Score](https://badge42.herokuapp.com/api/project/gdi-lore/ft_linear_regression)](https://github.com/JaeSeoKim/badge42)

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

<img src="https://render.githubusercontent.com/render/math?math=B = (max(X), (\overline{\theta_0} %2B \overline{\theta_1})(max(Y) - min(Y)) %2B min(Y))">

A questo punto otteniamo la retta passante per i due punti:

<img src="https://render.githubusercontent.com/render/math?math=\frac{x - x_A}{x_B - x_A} = \frac{y - y_A}{y_B - y_A}">

<img src="https://render.githubusercontent.com/render/math?math=\frac{x - min(X)}{max(X) - min(X)} = \frac{y - \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y)}{(\overline{\theta_0} %2B \overline{\theta_1})(max(Y) - min(Y)) %2B min(Y) - \overline{\theta_0}(max(Y) - min(Y)) - min(Y)}"> 

Elimiamo i fattori equivalenti dal denominatore della parte destra dell'uguaglianza: 

<img src="https://render.githubusercontent.com/render/math?math=\frac{x - min(X)}{max(X) - min(X)} = \frac{y - \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y)}{\overline{\theta_1}(max(Y) - min(Y))}">

Separiamo le somme al numeratore:

<img src="https://render.githubusercontent.com/render/math?math=\frac{x}{max(X) - min(X)} - \frac{min(X)}{max(X) - min(X)} = \frac{y}{\overline{\theta_1}(max(Y) - min(Y))} - \frac{\overline{\theta_0}(max(Y) - min(Y))}{\overline{\theta_1}(max(Y) - min(Y))} %2B \frac{min(Y)}{\overline{\theta_1}(max(Y) - min(Y))}">

Eliminiamo i fattori comuni nel secondo addendo della parte destra dell'uguaglianza: 

<img src="https://render.githubusercontent.com/render/math?math=\frac{x}{max(X) - min(X)} - \frac{min(X)}{max(X) - min(X)} = \frac{y}{\overline{\theta_1}(max(Y) - min(Y))} - \frac{\overline{\theta_0}}{\overline{\theta_1}} %2B \frac{min(Y)}{\overline{\theta_1}(max(Y) - min(Y))}">

Riorganizziamo l'equazione per farla apparire come la forma canonica della retta:

<img src="https://render.githubusercontent.com/render/math?math=\frac{y}{\overline{\theta_1}(max(Y) - min(Y))} = \frac{x}{max(X) - min(X)} - \frac{min(X)}{max(X) - min(X)} %2B \frac{\overline{\theta_0}}{\overline{\theta_1}} %2B \frac{min(Y)}{\overline{\theta_1}(max(Y) - min(Y))}">

Moltiplichiamo ambo i membri per il denominatore della parte sinistra dell'equazione:

<img src="https://render.githubusercontent.com/render/math?math=y = x\overline{\theta_1}\frac{(max(Y) - min(Y))}{max(X) - min(X)} - \frac{min(X)\overline{\theta_1}(max(Y) - min(Y))}{max(X) - min(X)} %2B \frac{\overline{\theta_0}\overline{\theta_1}(max(Y) - min(Y))}{\overline{\theta_1}} %2B \frac{min(Y)\overline{\theta_1}(max(Y) - min(Y))}{\overline{\theta_1}(max(Y) - min(Y))}">

Riduciamo il riducibile:

<img src="https://render.githubusercontent.com/render/math?math=y = x\overline{\theta_1}\frac{(max(Y) - min(Y))}{max(X) - min(X)} - \frac{min(X)\overline{\theta_1}(max(Y) - min(Y))}{max(X) - min(X)} %2B \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y)">

Da questa equazione otteniamo il coefficiente angolare <img src="https://render.githubusercontent.com/render/math?math=\theta_1"> e l'intercetta <img src="https://render.githubusercontent.com/render/math?math=\theta_0">:

<img src="https://render.githubusercontent.com/render/math?math=\theta_1 = \overline{\theta_1}\frac{(max(Y) - min(Y))}{max(X) - min(X)}">

<img src="https://render.githubusercontent.com/render/math?math=\theta_0 = \overline{\theta_0}(max(Y) - min(Y)) %2B min(Y) - min(X)\overline{\theta_1}\frac{max(Y) - min(Y)}{max(X) - min(X)}">
