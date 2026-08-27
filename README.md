# is_user_group_matrix

Ajoute un tableau croisé (utilisateurs × groupes de sécurité) dans
Réglages > Utilisateurs > **Matrice Utilisateurs / Groupes**, pour voir
d'un coup d'œil quels groupes sont attribués à chaque utilisateur — plutôt
que d'ouvrir chaque fiche utilisateur une par une.

## Utilisation

- **Vue pivot** (par défaut) : utilisateurs en colonne, groupes en ligne.
  Cliquer sur une cellule affiche le détail de la ligne correspondante.
- **Vue liste** : chaque ligne est une association utilisateur/groupe,
  avec un bouton "Ouvrir" qui va directement au formulaire complet de
  l'utilisateur (droits d'accès).
- Filtres/regroupements disponibles : par utilisateur, par groupe, par
  catégorie de groupe.

## Filtrage des données affichées

La matrice n'affiche que les groupes "pertinents" pour ne pas noyer
l'information :

- Utilisateurs actifs uniquement (`u.active = true`), hors utilisateurs
  portail/partagés (`u.share = false`).
- Exclut les comptes techniques `OdooBot` et l'administrateur système
  (`id` 1 et 2).
- Exclut les groupes techniques : seuls les groupes rattachés à une
  catégorie de module **visible** (`c.visible = true`) et ayant un
  **parent** sont retenus (ex. "Comptabilité / Facturation", pas les
  groupes internes sans catégorie affichée).

## Implémentation technique

`is.user.group.matrix` est un modèle **`_auto = False`** : ce n'est pas
une table, mais une **vue SQL** (recréée dans `init()`, à chaque mise à
jour du module) qui fait la jointure entre `res_users`, `res_groups` et
`ir_module_category`. Aucune donnée n'est dupliquée — la matrice reflète
toujours l'état actuel des droits, en lecture seule (liste non éditable,
non créable, non supprimable).
