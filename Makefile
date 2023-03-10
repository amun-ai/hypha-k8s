
prod:
	helmsman --debug -f helmsman.yaml --subst-env-values --apply --always-upgrade
staging:
	helmsman --debug --group staging -f helmsman.yaml --subst-env-values --apply --always-upgrade
staging.dry:
	helmsman --debug --group staging -f helmsman.yaml --subst-env-values --dry-run --always-upgrade
set.dot.env:
	set -o allexport; source ./secrets.env; set +o allexport
local.test:
	act --secret-file secrets.yaml
