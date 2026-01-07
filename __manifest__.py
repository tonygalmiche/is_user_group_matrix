# -*- coding: utf-8 -*-
{
    'name': 'Matrice Utilisateurs / Groupes',
    'version': '18.0.1.0.0',
    'author' : 'InfoSaône / Tony Galmiche',
    'category' : 'InfoSaône',
    'summary': 'Tableau croisé des utilisateurs et de leurs groupes de sécurité',
    'description': """
        Ce module ajoute une vue matricielle dans Paramètres / Utilisateurs
        permettant de visualiser les groupes de sécurité attribués à chaque utilisateur.
    """,
    'author': 'InfoSaône',
    'website': 'https://www.infosaone.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/is_user_group_matrix_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
