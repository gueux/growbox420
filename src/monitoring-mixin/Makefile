OUTPUT_DIR=./mixin_output/

all: clean dashboards rules alerts 

dashboards:
	jsonnet -J vendor -m ${OUTPUT_DIR} -e '(import "mixin.libsonnet").grafanaDashboards'

rules:
	jsonnet -J vendor -S -e 'std.manifestYamlDoc((import "mixin.libsonnet").prometheusRules)' > ${OUTPUT_DIR}/kubernetes_mixin_rules.yaml

alerts:
	jsonnet -J vendor -S -e 'std.manifestYamlDoc((import "mixin.libsonnet").prometheusAlerts)' > ${OUTPUT_DIR}/kubernetes_mixin_alerts.yaml

clean:
	rm -rf ${OUTPUT_DIR} && mkdir -p ${OUTPUT_DIR}