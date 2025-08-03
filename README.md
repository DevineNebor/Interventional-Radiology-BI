# Medical BI - Business Intelligence pour Services Médicaux

## Description

Medical BI est une application SaaS de Business Intelligence modulaire conçue spécifiquement pour les services médicaux réalisant des actes cliniques ou interventionnels (radiologie, cardiologie, blocs opératoires, endoscopie, etc.).

L'application permet de suivre l'activité médicale, gérer les ressources et générer des rapports détaillés pour optimiser l'organisation des services de santé.

## Fonctionnalités

### 🏥 Gestion de l'activité médicale
- **Suivi des actes** : Enregistrement des procédures avec durée, ressources utilisées et événements indésirables
- **Saisie simplifiée** : Interface rapide pour les manipulateurs, médecins et soignants
- **Import CSV** : Import en lot des données d'activité
- **Saisie manuelle** : Formulaire post-acte ou en fin de journée

### 📊 Tableaux de bord interactifs
- **KPI en temps réel** : Nombre d'actes, durée moyenne, occupation des salles
- **Filtres dynamiques** : Par période, salle, professionnel, type d'acte
- **Visualisations** : Graphiques et tableaux de bord personnalisables
- **Export** : Rapports PDF et Excel

### ⚙️ Configuration modulaire
- **Types d'actes configurables** : Chaque service peut définir ses propres procédures
- **Gestion des salles** : Configuration des équipements et capacités
- **Équipes médicales** : Gestion des professionnels et rôles
- **KPI personnalisés** : Métriques adaptées à chaque spécialité

### 🔐 Sécurité et accès
- **Authentification** : Système de connexion sécurisé
- **Gestion des rôles** : Admin et utilisateur avec permissions différenciées
- **Audit trail** : Traçabilité des actions et modifications

## Stack technique

### Backend
- **Framework** : FastAPI (Python)
- **Base de données** : SQLite (développement) / PostgreSQL (production)
- **ORM** : SQLAlchemy
- **Authentification** : JWT avec bcrypt
- **Documentation** : Swagger/OpenAPI automatique

### Frontend
- **Framework** : React 18 avec TypeScript
- **Styling** : Tailwind CSS
- **Routing** : React Router DOM
- **Charts** : Chart.js avec react-chartjs-2
- **Forms** : React Hook Form
- **Build** : Vite

### Infrastructure
- **Conteneurisation** : Docker et Docker Compose
- **Base de données** : PostgreSQL 15
- **Déploiement** : Sans serveur HDS requis

## Lancement (Docker)

### Prérequis
- Docker et Docker Compose installés
- Git

### Installation et démarrage

1. **Cloner le repository**
```bash
git clone <repository-url>
cd medical-bi
```

2. **Configurer l'environnement**
```bash
cp .env.example .env
# Modifier les variables dans .env si nécessaire
```

3. **Lancer l'application**
```bash
cd docker
docker-compose up -d
```

4. **Accéder à l'application**
- Frontend : http://localhost:3000
- Backend API : http://localhost:8000
- Documentation API : http://localhost:8000/docs

### Compte par défaut
- **Email** : admin@medical-bi.com
- **Mot de passe** : admin123

### Développement local

#### Backend
```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur de développement
uvicorn app.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Structure du projet

```
medical-bi/
├── app/                    # Backend FastAPI
│   ├── api/               # Routes API
│   ├── models/            # Modèles SQLAlchemy
│   ├── schemas/           # Schémas Pydantic
│   ├── services/          # Services métier
│   ├── utils/             # Utilitaires
│   └── config.py          # Configuration
├── frontend/              # Frontend React
│   ├── src/
│   │   ├── components/    # Composants React
│   │   ├── pages/         # Pages de l'application
│   │   ├── services/      # Services API
│   │   └── styles/        # Styles CSS
│   └── package.json
├── docker/                # Configuration Docker
├── tests/                 # Tests unitaires et d'intégration
└── README.md
```

## Base de données

### Tables principales
- **users** : Utilisateurs et authentification
- **procedures** : Actes médicaux réalisés
- **rooms** : Salles et équipements
- **professionals** : Équipe médicale
- **procedure_types** : Types d'actes configurables

### Relations
- Chaque procédure est liée à un type d'acte, une salle et un professionnel
- Les salles et professionnels sont organisés par service
- Les types d'actes sont configurables par service

## Roadmap

### Phase 1 - MVP (Actuelle)
- [x] Authentification et gestion des utilisateurs
- [x] CRUD des procédures, salles, professionnels
- [x] Dashboard avec KPI de base
- [x] Interface de saisie simplifiée
- [ ] Import CSV des données
- [ ] Export PDF/Excel

### Phase 2 - Fonctionnalités avancées
- [ ] Graphiques interactifs avec Chart.js
- [ ] Filtres avancés et recherche
- [ ] Notifications et alertes
- [ ] Gestion des événements indésirables
- [ ] Rapports mensuels automatisés

### Phase 3 - Optimisations
- [ ] Cache Redis pour les performances
- [ ] API rate limiting
- [ ] Logs et monitoring
- [ ] Tests automatisés complets
- [ ] Documentation utilisateur

### Phase 4 - Évolutions
- [ ] Multi-tenant pour plusieurs établissements
- [ ] API mobile pour saisie sur tablette
- [ ] Intégration avec systèmes hospitaliers
- [ ] Intelligence artificielle pour prédictions
- [ ] Tableaux de bord personnalisables

## Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Support

Pour toute question ou support :
- Ouvrir une issue sur GitHub
- Contacter l'équipe de développement

---

**Medical BI** - Optimisez votre activité médicale avec des données intelligentes.