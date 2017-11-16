# IA-QUARTO

commandes essentielles pour git:

git pull : Si vous travaillez sur votre ordinateur local, et que vous voulez la version la plus à jour de votre repository pour travailler dessus, vous “pull”ez (tirez) les modifications provenant de Github avec cette commande.

git commit : la commande la plus importante de Git. Après avoir effectué toute sorte de modification, vous entrez ça afin de prendre un “instantané” du dépôt. Généralement cela s’écrit sous la forme git commit -m “Message ici“. Le -m indique que la section suivante de la commande devrait être lue comme un message.

git push : Si vous travaillez sur votre ordinateur local, et voulez que vos commits soient visibles aussi en ligne sur Github, vous « push »ez les modifications vers Github avec cette commande.


méthode:
- je mets à jour mon répertoire: git pull
- j'effectue des modifications, en faisant régulièrement des commits (à des moments utiles et lorsque cela fonctionne)
- je finis en envoyant mes modifications au monde: git push

PS: il peut arriver que d'autres travaillent au même moment, alors faites des git pull regulièrement et en cas de conflits faites de votre mieux.
A notre niveau il n'est peut-être pas nécessaire de faire plusieurs branches.