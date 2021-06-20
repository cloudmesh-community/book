# Inventory

Sometimes it is necessary to maintain a simple inventory. Naturally, if you
know python you can do this with dicts. However to manage a large number
of items with repeated values its is of advantage to do this from the
command line.

We have written such a tool that lets you easily manage the resources in
a table format. If you need additional features, help us improve them or
tell us about your needs.


## Configuration

Your inventory will be located at

`~/.cloudmesh/inventory.yaml`

You can also change the YAML file by hand, but the cm command is more convenient.

An example file will look as follows:

```
g001:
  cluster: gregor
  comment: test
  host: g001
  ip: 127.0.0.1
  label: g001
  metadata: None
  name: g001
  owners: gvonlasz
  project: cloudmesh
  service: compute
g002:
  cluster: gregor
  comment: test
  host: g002
  ip: 127.0.0.1
  label: g002
  metadata: None
  name: g002
  owners: gvonlasz
  project: cloudmesh
  service: compute
```

For more features, please see the [README](https://github.com/cloudmesh/cloudmesh-inventory/blob/master/README.md)

## Manual Page

```
Usage:
    inventory add NAMES [--label=LABEL]
                        [--service=SERVICES]
                        [--project=PROJECT]
                        [--owners=OWNERS]
                        [--comment=COMMENT]
                        [--cluster=CLUSTER]
                        [--ip=IP]
    inventory set NAMES ATTRIBUTE to VALUES
    inventory delete NAMES
    inventory clone NAMES from SOURCE
    inventory list [NAMES] [--format=FORMAT] [--columns=COLUMNS]
    inventory info

Arguments:

  NAMES     Name of the resources (example i[10-20])

  FORMAT    The format of the output is either txt,
            yaml, dict, table [default: table].

  OWNERS    a comma-separated list of owners for this resource

  LABEL     a unique label for this resource

  SERVICE   a string that identifies the service

  PROJECT   a string that identifies the project

  SOURCE    a single hostname to clone from

  COMMENT   a comment

Options:

   -v       verbose mode

Description:

      add -- adds a resource to the resource inventory

      list -- lists the resources in the given format

      delete -- deletes objects from the table

      clone -- copies the content of an existing object
               and creates new ones with it

      set   -- sets for the specified objects the attribute to the given value or values. If multiple values are used the values are assigned to the and objects in order. See examples

      map   -- allows setting attributes on a set of objects
               with a set of values

Examples:

  cm inventory add x[0-3] --service=openstack

      adds hosts x0, x1, x2, x3 and puts the string
      OpenStack into the service column

  cm lits

      lists the repository

  cm x[3-4] set temperature to 32

      sets for the resources x3, x4 the value of the
      temperature to 32

  cm x[7-8] set ip 128.0.0.[0-1]

      sets the value of x7 to 128.0.0.0
      sets the value of x8 to 128.0.0.1

  cm clone x[5-6] from x3

      clones the values for x5, x6 from x3
```
