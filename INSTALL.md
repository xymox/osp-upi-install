# Setup

## Host setup

````
% sudo yum -y install python-dns
````


## Create DNS zone

openstack zone create

or through Horizon if you don't have designate extension for openstack client


## Create floating ips

````
openstack floating ip create --dns-name "api" --dns-domain "cluster-acm.openshift-v4.dcpro31.opk.recouv." --description "API cluster-acm.openshift-v4.dcpro31.opk.recouv" CNP31-OPK-MGT-GIDN-01
openstack floating ip create --dns-name "*.apps" --dns-domain "cluster-acm.openshift-v4.dcpro31.opk.recouv." --description "APPS cluster-acm.openshift-v4.dcpro31.opk.recouv" CNP31-OPK-MGT-GIDN-01
````

## Adjust cluster.yml

First of all, you need to adjust cluster.yml (using cluster-example.yml) to fit your infrastructure configuration.

## Create installation files

Run

````
% ./ansible/02-create-cluster.yaml
````

to create install-config.yaml and then manifests and ignition config files for the infrastructure.


## Create OSP network and resources

