#!/bin/bash

export CC_PROJECTID="CH-819337"
export CC_PREFIX="NNN-albert" # repalce with your firtsname and hid number

export OS_AUTH_URL=https://openstack.tacc.chameleoncloud.org:5000/v2.0
# With Keystone you pass the keystone password.
echo "Please enter your OpenStack Password: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT

export OS_TENANT_ID=$CC_PROJECTID
export OS_TENANT_NAME=$CC_PROJECTID
export OS_PROJECT_NAME=$CC_PROJECTID
export OS_USERNAME="<put your chameleon cloud username here>"


export OS_REGION_NAME="RegionOne"
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi