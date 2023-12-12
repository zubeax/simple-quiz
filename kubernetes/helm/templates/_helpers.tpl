{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "simple-quiz.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "simple-quiz.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "simple-quiz.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "simple-quiz.labels" -}}
helm.sh/chart: {{ include "simple-quiz.chart" . }}
{{ include "simple-quiz.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "simple-quiz.selectorLabels" -}}
app.kubernetes.io/name: {{ include "simple-quiz.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Create the name of the service account to use
*/}}
{{- define "simple-quiz.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
    {{ default (include "simple-quiz.fullname" .) .Values.serviceAccount.name }}
{{- else -}}
    {{ default "default" .Values.serviceAccount.name }}
{{- end -}}
{{- end -}}

{{- define "simple-quiz.clusterType" -}}
{{ $clusterType := default .Values.global.clusterType .Values.clusterType }}
{{- if or (eq $clusterType "openshift") (regexFind "^ocp.*" $clusterType) -}}
{{- "openshift" -}}
{{- else -}}
{{- "kubernetes" -}}
{{- end -}}
{{- end -}}

{{- define "simple-quiz.route-port" -}}
{{- if .Values.sso.enabled -}}
{{ printf "proxy" }}
{{- else -}}
{{ printf "http" }}
{{- end -}}
{{- end -}}

{{- define "simple-quiz.route-termination" -}}
{{- if .Values.sso.enabled -}}
{{ printf "reencrypt" }}
{{- else -}}
{{ printf "edge" }}
{{- end -}}
{{- end -}}
