#!/bin/bash

verb=install
cns=--create-namespace
dryrun=''
valuefile='-f ./helm/values.yaml'
templates='./helm'

ns=simple-quiz
svc=simple-quiz

    while [[ "${1}" =~ ^-.* ]]
    do
        case "${1}" in
            --help|-h)
                echo "usage: $(basename ${0}) [--upgrade] [--delete] [--dry-run] [-h]"
                exit 1
                shift;;
            --upgrade|-u)
                verb=upgrade
                cns=''
                shift;;
            --delete)
                verb=delete
                cns=''
                valuefile=''
                templates=''
                shift;;
            --dry-run|--dryrun|-d)
                dryrun='--dry-run'
                shift;;
            *)  shift;;
        esac
    done

    helm $verb $svc --namespace $ns $cns $dryrun $valuefile $templates

exit 0

