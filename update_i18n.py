import json
import os

items_en = [
    {
        "date": "Jun 2025 – Dec 2025",
        "title": "Master's Thesis: Trustworthy LLMs in Industrial Contexts",
        "company": "Siemens",
        "location": "Munich, Bavaria, Germany",
        "image": "assets/siemens.jpeg",
        "description": "Built a vision-based RAG pipeline to generate CAM machining sequences, alongside a custom evaluation framework to ensure AI safety. Leveraged attention layer metrics to guarantee the reliable propagation of data redactions, effectively eliminating hallucinations and safeguarding confidential metadata in industrial deployments.",
        "skills": [
            "Large Language Models (LLMs)", 
            "Vision-Language Models (VLAs)", 
            "Retrieval-Augmented Generation (RAG)", 
            "AI Safety", 
            "Python", 
            "Computer Vision"
        ]
    },
    {
        "date": "Oct 2021 – Dec 2025",
        "title": "Working Student – AI/ML & SafeMLOps",
        "company": "Siemens",
        "location": "Munich, Bavaria, Germany",
        "image": "assets/siemens.jpeg",
        "description": "Engineered a company-wide SafeMLOps Python template (utilizing Copier and Jinja) to standardize CI/CD, security scanning, and GPU-enabled model training across multiple engineering teams.\n\nMaintained and optimized a U-Net CNN for image segmentation at Siemens Mobility, leveraging DVC and cross-platform dependency management (Poetry) to reduce false positive calls.\n\nModernized complex legacy codebases and successfully delivered critical model robustness and certification evaluations for the annual Siemens AI Summit.",
        "skills": [
            "Deep Learning", 
            "Linux", 
            "Python", 
            "PyTorch", 
            "TensorFlow", 
            "Computer Vision", 
            "CI/CD", 
            "MLOps"
        ]
    },
    {
        "date": "May 2022 – Sep 2022",
        "title": "Bachelor Thesis - Certification of Model's Robustness against Natural Perturbations",
        "company": "Siemens",
        "location": "Munich, Bavaria, Germany",
        "image": "assets/siemens.jpeg",
        "description": "Completed my Bachelor's thesis on \u201cModel Certification Against Natural Perturbations\u201d, aligned with compliance requirements from the upcoming EU AI Act. The work focused on optimizing and parallelizing methods to determine the extent of natural perturbations that lead to misclassification or segmentation errors.",
        "skills": [
            "AI Compliance", 
            "Model Robustness", 
            "Python", 
            "Parallel Programming", 
            "Machine Learning"
        ]
    },
    {
        "date": "Mar 2022 – Sep 2022",
        "title": "Intern Prototype Development",
        "company": "BMW Group",
        "location": "Munich, Bavaria, Germany",
        "image": "assets/bmw.png",
        "description": "Evaluation of a new car login concept, NDA. Proof-of-Concept utilizing Bluetooth Low Energy (BLE) and a secure AWS-based backend.",
        "skills": [
            "Android", 
            "AWS", 
            "Kotlin", 
            "C++", 
            "Python", 
            "Bluetooth Low Energy", 
            "Mobile Apps"
        ]
    },
    {
        "date": "Jun 2014 – Jan 2019",
        "title": "Founder @ ROTOR",
        "company": "ROTOR",
        "location": "Fontainebleau, Île-de-France, France",
        "description": "Founded an organization specializing in the design, refinement, and manufacturing of state-of-the-art FPV and UAV drones.\nBuilt and deployed over 30 custom drones, including advanced hexacopters for professional photography clients.\n\nRegistered as a non-profit organization under the French Law of 1 July 1901 (Association Loi 1901).",
        "skills": [
            "Drone Piloting", 
            "Electronics", 
            "CAD", 
            "Blender", 
            "Python", 
            "Web Development", 
            "Prototyping"
        ]
    }
]

items_fr = [
    {
        "date": "Juin 2025 – Déc 2025",
        "title": "Mémoire de Master : LLM fiables dans des contextes industriels",
        "company": "Siemens",
        "location": "Munich, Bavière, Allemagne",
        "image": "assets/siemens.jpeg",
        "description": "Création d'un pipeline RAG basé sur la vision afin de générer des séquences d'opérations d'usinage à partir de données CAM, accompagné d'un cadre d'évaluation personnalisé pour garantir la sécurité de l'IA. Utilisation de métriques de couches d'attention pour garantir la propagation fiable des rédactions de données, éliminant efficacement les hallucinations et protégeant les métadonnées confidentielles lors des déploiements industriels.",
        "skills": [
            "Grands Modèles de Langage (LLM)", 
            "Modèles Vision-Langage (VLA)", 
            "Génération Augmentée par la Recherche (RAG)", 
            "Sécurité de l'IA", 
            "Python", 
            "Vision par ordinateur"
        ]
    },
    {
        "date": "Oct 2021 – Déc 2025",
        "title": "Étudiant en emploi – AI/ML & SafeMLOps",
        "company": "Siemens",
        "location": "Munich, Bavière, Allemagne",
        "image": "assets/siemens.jpeg",
        "description": "Conception d'un modèle Python SafeMLOps à l'échelle de l'entreprise (utilisant Copier et Jinja) pour standardiser la CI/CD, l'analyse de sécurité et l'entraînement de modèles activés par GPU au sein de plusieurs équipes d'ingénierie.\n\nMaintien et optimisation d'un CNN U-Net pour la segmentation d'images chez Siemens Mobility, en tirant parti de DVC et de la gestion des dépendances multiplateformes (Poetry) pour réduire les faux positifs.\n\nModernisation de bases de code complexes héritées et livraison avec succès d'évaluations cruciales sur la robustesse et la certification des modèles pour le sommet annuel de l'IA de Siemens.",
        "skills": [
            "Deep Learning", 
            "Linux", 
            "Python", 
            "PyTorch", 
            "TensorFlow", 
            "Vision par ordinateur", 
            "CI/CD", 
            "MLOps"
        ]
    },
    {
        "date": "Mai 2022 – Sep 2022",
        "title": "Mémoire de Licence - Certification de la Robustesse des Modèles contre les Perturbations Naturelles",
        "company": "Siemens",
        "location": "Munich, Bavière, Allemagne",
        "image": "assets/siemens.jpeg",
        "description": "Réalisation de mon mémoire de Licence sur la \u00ab Certification des Modèles contre les Perturbations Naturelles \u00bb, en alignement avec les exigences de conformité du futur règlement européen sur l'IA (EU AI Act). Le travail s'est concentré sur l'optimisation et la parallélisation des méthodes pour déterminer l'étendue des perturbations naturelles conduisant à des erreurs de classification ou de segmentation.",
        "skills": [
            "Conformité de l'IA", 
            "Robustesse des Modèles", 
            "Python", 
            "Programmation Parallèle", 
            "Machine Learning"
        ]
    },
    {
        "date": "Mar 2022 – Sep 2022",
        "title": "Stagiaire Développement de Prototype",
        "company": "BMW Group",
        "location": "Munich, Bavière, Allemagne",
        "image": "assets/bmw.png",
        "description": "Évaluation d'un nouveau concept de connexion de voiture, sous NDA. Preuve de concept (PoC) utilisant le Bluetooth Low Energy (BLE) et un backend sécurisé basé sur AWS.",
        "skills": [
            "Android", 
            "AWS", 
            "Kotlin", 
            "C++", 
            "Python", 
            "Bluetooth Low Energy", 
            "Applications Mobiles"
        ]
    },
    {
        "date": "Juin 2014 – Janv 2019",
        "title": "Fondateur @ ROTOR",
        "company": "ROTOR",
        "location": "Fontainebleau, Île-de-France, France",
        "description": "Fondation d'une organisation spécialisée dans la conception, le perfectionnement et la fabrication de drones FPV et UAV de pointe.\nConstruit et déployé de plus de 30 drones personnalisés, dont des hexacoptères avancés pour des clients professionnels de la photographie.\n\nEnregistrée comme organisation à but non lucratif sous la loi française du 1er juillet 1901 (Association Loi 1901).",
        "skills": [
            "Pilotage de drones", 
            "Électronique", 
            "CAO", 
            "Blender", 
            "Python", 
            "Développement Web", 
            "Prototypage"
        ]
    }
]

items_de = [
    {
        "date": "Jun 2025 – Dez 2025",
        "title": "Masterarbeit: Vertrauenswürdige LLMs in industriellen Kontexten",
        "company": "Siemens",
        "location": "München, Bayern, Deutschland",
        "image": "assets/siemens.jpeg",
        "description": "Aufbau einer visionsbasierten RAG-Pipeline zur Generierung von CAM-Bearbeitungssequenzen, flankiert von einem maßgeschneiderten Evaluierungs-Framework zur Gewährleistung der KI-Sicherheit. Nutzung von Attention-Layer-Metriken, um die zuverlässige Weitergabe von Datenredaktionen zu garantieren, Halluzinationen effektiv zu eliminieren und vertrauliche Metadaten in industriellen Einsatzgebieten zu schützen.",
        "skills": [
            "Große Sprachmodelle (LLMs)", 
            "Vision-Language-Modelle (VLAs)", 
            "Retrieval-Augmented Generation (RAG)", 
            "KI-Sicherheit", 
            "Python", 
            "Computer Vision"
        ]
    },
    {
        "date": "Okt 2021 – Dez 2025",
        "title": "Werkstudent – AI/ML & SafeMLOps",
        "company": "Siemens",
        "location": "München, Bayern, Deutschland",
        "image": "assets/siemens.jpeg",
        "description": "Entwicklung einer unternehmensweiten SafeMLOps-Python-Vorlage (unter Verwendung von Copier und Jinja) zur Standardisierung von CI/CD, Sicherheits-Scans und GPU-gestütztem Modelltraining über mehrere Engineering-Teams hinweg.\n\nWartung und Optimierung eines U-Net-CNNs zur Bildsegmentierung bei Siemens Mobility, mit Einsatz von DVC und plattformübergreifendem Abhängigkeitsmanagement (Poetry) zur Reduzierung falsch-positiver Meldungen.\n\nModernisierung komplexer Legacy-Codebases und erfolgreiche Lieferung kritischer Modellrobustheits- und Zertifizierungsevaluationen für den jährlichen Siemens AI Summit.",
        "skills": [
            "Deep Learning", 
            "Linux", 
            "Python", 
            "PyTorch", 
            "TensorFlow", 
            "Computer Vision", 
            "CI/CD", 
            "MLOps"
        ]
    },
    {
        "date": "Mai 2022 – Sep 2022",
        "title": "Bachelorarbeit - Zertifizierung der Modellrobustheit gegen natürliche Störungen",
        "company": "Siemens",
        "location": "München, Bayern, Deutschland",
        "image": "assets/siemens.jpeg",
        "description": "Verfassen der Bachelorarbeit über \u201eModellzertifizierung gegen natürliche Störungen\u201c, in Übereinstimmung mit den Compliance-Anforderungen des kommenden EU AI Act. Die Arbeit fokussierte sich auf die Optimierung und Parallelisierung von Methoden zur Bestimmung des Ausmaßes natürlicher Störungen, die zu Fehlklassifikationen oder Segmentierungsfehlern führen.",
        "skills": [
            "KI-Compliance", 
            "Modellrobustheit", 
            "Python", 
            "Parallele Programmierung", 
            "Machine Learning"
        ]
    },
    {
        "date": "Mär 2022 – Sep 2022",
        "title": "Praktikant Prototypenentwicklung",
        "company": "BMW Group",
        "location": "München, Bayern, Deutschland",
        "image": "assets/bmw.png",
        "description": "Bewertung eines neuen Fahrzeug-Login-Konzepts, NDA. Proof-of-Concept unter Verwendung von Bluetooth Low Energy (BLE) und einem sicheren AWS-basierten Backend.",
        "skills": [
            "Android", 
            "AWS", 
            "Kotlin", 
            "C++", 
            "Python", 
            "Bluetooth Low Energy", 
            "Mobile Apps"
        ]
    },
    {
        "date": "Jun 2014 – Jan 2019",
        "title": "Gründer @ ROTOR",
        "company": "ROTOR",
        "location": "Fontainebleau, Île-de-France, Frankreich",
        "description": "Gründung einer Organisation, die sich auf das Design, die Weiterentwicklung und Herstellung von hochmodernen FPV- und UAV-Drohnen spezialisiert hat.\nBau und Einsatz von über 30 maßgeschneiderten Drohnen, einschließlich fortschrittlicher Hexakopter für professionelle Kunden aus der Fotografie.\n\nEingetragen als gemeinnützige Organisation nach französischem Recht vom 1. Juli 1901 (Association Loi 1901).",
        "skills": [
            "Drohnensteuerung", 
            "Elektronik", 
            "CAD", 
            "Blender", 
            "Python", 
            "Webentwicklung", 
            "Prototyping"
        ]
    }
]

base_path = "/Users/shannah/Documents/OTHER/SH2282000.github.io/i18n"

for lang, items in [("en", items_en), ("fr", items_fr), ("de", items_de)]:
    filepath = os.path.join(base_path, f"{lang}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    if "resume" in data and "items" in data["resume"]:
        data["resume"]["items"] = items
        
    json_str = json.dumps(data, indent=4, ensure_ascii=False)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json_str + "\n")
        
print("Updated all JSON files successfully with skills.")
