import streamlit as st


title = "Description Détaillée du Projet"
sidebar_name = "Description Détaillée du Projet"


def run():

    st.title(title)
    st.markdown("---")

    st.write("### A - Cahier des Charges")

    st.write(":green[1 - Choix du Sujet et des Modèles]")
    st.markdown("* Nous avons repris le sujet de prédiction de satisfaction clientèle réalisé pour le projet de formation Data Scientist.")
    st.write(
        """ * Nous avons sélectionné 3 modèles réalisés sur 8, pour leurs différences de preprocessing & modélisation, bien qu'aucun ne soit optimisé :
    * un Gradient Boosting Classifier :red[GBC]
    * un Support Vector Machine appliqué sur un modèle pré-entainé wikipedia2vec :red[SVM]
    * un Artificial Neuronal Network :red[ANN] appliqué aussi sur wikipedia2vec""")

    st.write(":green[2 - Définition des Métriques et Exigences de Performances]")
    st.write(
        """ * Notre choix s'est porté sur les métriques d':red[accuracy] et de :red[F1-score] que nous souhaitons :red[> 80%] pour commencer""")

    st.write(":green[3 - Schéma d'Implantation]")
    st.write(""" * Nous utilisons
    * :red[FastApi] en back-end pour la gestion de notre base de données et sa mise-à-jour
    * :red[Airflow] pour le preprocessing, fit & classification_report des modèles mis-à-jour
    * :red[Streamlit] en front-end pour présenter notre projet, comprendre ses problématiques et améliorations envisagées,
    ainsi que de permettre des "prédictions à la demande" et vérifier si nos exigences de métriques sont respectées""")
    st.image("/airflow/data_others/JPG-PNG/schema_implantation.png")

    st.write("### B - Version Control, Tests Unitaires & Installation")   ######  modif 1--------------------------------------

    st.write(":green[1 - Git / GitHub]")
    st.write(
        """ * Nous avons créé un Repository Github sous :blue[*https://github.com/Fred-Zang/mlops_projet2.git*]
    * La procédure de commits s'est effectuée sur un découpage du code en de nombreuses petites parties, sur différentes branches, pour permettre à chacun d'agir indépendamment""")
    st.image("/airflow/data_others/JPG-PNG/git_branch_commits-quan-eric-fred.png")

    st.write("")

    st.write(":green[2 - Tests Unitaires]")
    st.write(
        """ * Nous utilisons :red[GitHub Actions] pour créer :red[2 workflows] de vérification de nos codes lors des push de nos commits sur Github.

    * le fichier :blue[.github/workflows/python-app.yml] dans notre arborescence permet de lancer automatiquement les test :red[PEP8] et :red[Pytest] sur tous nos codes Python.""")
    st.image("/airflow/data_others/JPG-PNG/tests_unitaires.png")
    st.write("")

    st.write(":green[3 - Procédure d'Utilisation & Installation]")
    st.write(
        """ * Toutes les Procédures d'Utilisation, d'Installation et Commandes terminale nécessaires sont décrites dans le :red[README.md] du repo GitHub""")

    st.write("")
    st.write("### C - Interfaces utilisées et Arborescences mises en place")
    st.write("")
     
     
    st.write(":green[1 - API - gestion de la base de données]")
    st.write(
        """ * La gestion de notre base de données d'entrainement des modèles est gérée en back-end par le framework :red[FastAPI]
    * Nous implémentons une :red[Authentification des Utilisateurs] Basic HTTP pour les users :orange[admin, user].
    * Les :red[password] sont identiques aux usernames pour des questions de facilité et peuvent être modifiés avec le fichier :orange[PyAPI.py]
    * L'accès à cette API s'effectue par un navigateur à l'adresse :blue[http://localhost:8000/docs].
    * Toutes les descriptions des :blue[EndPoints] et leurs usages sont données dans cet accès navigateur.""")

    st.image("/airflow/data_others/JPG-PNG/API-fastapi.png")

    st.write(
        """ * Le Endpoint :red[/comment] permet d'ajouter un commentaire et une notation directement dans :blue[data_MAJ.csv]""")

    st.write(
        """ * Le Endpoint :red[/uploadfile] est disponible uniquement pour le user :orange[admin].
    * 2 fichiers de tests d'ajout à la base de donnée data_MAJ.csv sont disponibles dans le sous-dossier :blue[airflow/clean_data/--new_data_test/new_data_test.csv])
    * il est conseillé de voir la procédure complète décrite dans README.md pour réaliser chaque étape dans le bon ordre puisque nous n'avons pas d'API de données récupérable automatiquement
    * un fichier de sauvegarde est enregistré pour une totale :red[traçabilité des mises à jour] des datas ajoutées.
    * le fichier :blue[data_MAJ.csv] est également remplacé par la mise à jour de données car c'est ce fichier qui est utilisé par la suite pour les MAJ de nos modèles.""")

    st.write("")
    st.write(
        ":green[2 - Airflow - Pipeline CI/CD] de :red[preprocessing->training->reporting->updating] des modèles")
    st.write(
        """ * L'accès à l'interface Airflow s'effectue par un navigateur à l'adresse :blue[http://localhost:8080].
    * Airflow récupère le fichier :blue[data_MAJ.csv] des données de la dernière mise à jour puis effectue les tâches suivantes sur nos 3 modèles :""")
    st.image("/airflow/data_others/JPG-PNG/Airflow-tasks.png")

    st.write(":green[3 - Streamlit]")

    st.write(
        """ *  L'accès à l'interface Streamlit s'effectue par un navigateur à l'adresse :blue[http://localhost:8501].
    * Nous nous en servons pour la présentation de notre projet
    * Nous développons les problématiques rencontrées et pistes d'améliorations trouvées
    * Une page :red[Prédictions à la demande] nous permet de tester chaque mise-à-jour de modèle
    * Une page :red[Visual Reporting et Alertes Performances] nous permet d'effectuer un suivi sur nos mises-à-jour""")

    st.write("")
    st.write(":green[4 - Arborescence des datas] utilisées et mise-à-jour")
    st.image("/airflow/data_others/JPG-PNG/datas_explications.png")

    st.write(":green[5 - Arborescence des modèles] utilisés et mise-à-jour")
    st.image("/airflow/data_others/JPG-PNG/bilan_modeles.png")



    st.write("### D - Isolation")

    st.write(":green[1 - Docker]")
    st.write(
        """ *  Fastapi, Airflow et Streamlit sont isolés par des :red[Dockerfiles séparés], chacun ayant son propre :orange[requirements.txt]
    * Dans le dossier de travail principal :blue[mlops_projet2], nous avons un :red[docker-compose] qui build les images de Fastapi et Streamlit dans :orange[2 containers disctincts]
    * Dans le sous-dossier :blue[airflow] nous avons un second :red[docker-compose] qui build l'image de Airflow contenant en tout :orange[7 containers]
    * Cette :red[isolation n'est pas optimisée en l'état] ( voir onglet suivant) et nous devons faire de nombreux tests encore pour résoudre ce point.""")

    st.write(":green[2 - DockerHub]")
    st.write(
        """ *  Vu la taille des images à construire et l'utilisation importante de ressources, nous avons décidé de mettre les :red[images à disposition].
    * Veuillez svp vous rendre dans :red[README.md pour suivre la procédure] à réaliser dans ce cas si votre PC local n'offre pas assez de ressources mémoire""")

    st.image("/airflow/data_others/JPG-PNG/dockerHub_fred.png")
    st.write(""" * *nom des images à renseigner dans les docker-compose* :
   *  fredzang/my_fastapi_mlops:2.0.0
   *  fredzang/my_streamlit_mlops:2.0.0
   *  fredzang/my_airflow_mlops:2.0.0""")

    st.write("### E - Options Supplémentaires à envisager")

    st.write(":green[1 - Déploiement Cloud]")
    st.write(
        """ *  Une solution pour :red[déporter nos problèmatiques] de poids d'images et ressources utilisées serait de déployer notre solution sur un service Cloud comme :orange[Amazon AWS ECS].
    * Nous préférons tout d'abord trouver de meilleurs solutions à notre déploiement""")
    st.image("/airflow/data_others/JPG-PNG/aws-ces.png")

    st.write(":green[2 - Orchestration Kubernetes]")
    st.write(
        """ * Enfin, un système open-source permettant d':red[automatiser le déploiement, la mise à l'échelle et la gestion des applications conteneurisées] serait un point final à réaliser.
    * Nous n'avons pas le temps nécessaire pour cela et bien des points d'améliorations à résoudre avant tout""")
    st.image("/airflow/data_others/JPG-PNG/kubernetes.png")
