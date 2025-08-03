#!/bin/bash

echo "🚀 Démarrage de Medical BI..."

# Vérifier si Docker est installé
if ! command -v docker &> /dev/null; then
    echo "❌ Docker n'est pas installé. Veuillez installer Docker d'abord."
    exit 1
fi

# Vérifier si Docker Compose est installé
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose n'est pas installé. Veuillez installer Docker Compose d'abord."
    exit 1
fi

# Copier le fichier d'environnement s'il n'existe pas
if [ ! -f .env ]; then
    echo "📝 Copie du fichier .env.example..."
    cp .env.example .env
    echo "✅ Fichier .env créé. Vous pouvez le modifier si nécessaire."
fi

# Aller dans le dossier docker
cd docker

# Démarrer les services
echo "🐳 Démarrage des services Docker..."
docker-compose up -d

# Attendre que les services soient prêts
echo "⏳ Attente du démarrage des services..."
sleep 10

# Vérifier le statut
echo "📊 Statut des services :"
docker-compose ps

echo ""
echo "🎉 Medical BI est prêt !"
echo ""
echo "📱 Frontend : http://localhost:3000"
echo "🔧 Backend API : http://localhost:8000"
echo "📚 Documentation API : http://localhost:8000/docs"
echo ""
echo "👤 Compte par défaut :"
echo "   Email : admin@medical-bi.com"
echo "   Mot de passe : admin123"
echo ""
echo "🛑 Pour arrêter : docker-compose down"