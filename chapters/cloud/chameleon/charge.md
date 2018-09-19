# Chameleon Cloud Charge Rates


It is important to fully understand the charge rates of your VM and
storage use.

Chameleon has two types of limitations, introduced to promote fair
resource usage to all:

Allocation:

:   Chameleon projects are limited to a per-project allocation currently
    set to 20,000 service units for 6 months. Allocations can be renewed
    or extended

Lease:

:   To ensure fairness to all users, resource reservations (leases) are
    limited to a duration of 7 days. However, an active lease within 48
    hours of its end time can be prolonged by up to 7 days from the
    moment of request if resources are available. To prolong a lease,
    click on the "Update Lease" button in the Reservations panel of the
    CHI OpenStack dashboard, and enter the additional duration requested
    in the "Prolong for" box including the unit suffix, e.g. "5d" for 5
    days or "30m" for 30 minutes. If there is an advance reservation
    blocking your lease prolongation that could potentially be moved,
    you can interact through the users mailing list to coordinate with
    others users. Additionally, if you know from the start that your
    lease will require longer than a week and can justify it, you can
    [contact Chameleon staff via the ticketing
    system](https://www.chameleoncloud.org/user/help/ticket/new/) to
    request a one-time exception to create a longer lease. The lease
    must be requested by the PI.

## Service Units


Chameleon allocations can consist of several components of the system.
Users can request allocation of individual compute nodes, storage
servers, or complete Scalable Compute Units (SCUs) which contain compute
servers, storage nodes, and an open flow switch.

Compute servers are allocated in Service Units (SUs), which equates to
one hour of wall clock time on a single server (for virtual machines, an
SU is 24 cores with up to 128GB of RAM). Note this unit differs from
traditional HPC or cloud service units that are charged in core-hours; a
Chameleon SU is a full server, as the type of experiments and
performance measurements users may wish to do may be contaminated by
sharing nodes.

Storage servers are also charged in SUs, at 2x the rate of compute
servers (i.e., 1 hour allocation of 1 storage server == 2 SUs). SCUs are
charged at the rate of 50 SUs per wall clock hour (42 compute servers, 4
storage nodes, plus one OpenFlow switch).

An allocation may make use of multiple SCUs, up to the size of the full
testbed.

For example, a user wishing to provision a 10 node cluster +1 storage
server for a 1 week experiment should budget
`[(10 + 2) SUs per hour]  [7 days  24 hours/day] = 2,016 SUs` for that
experiment.

SUs are charged the same regardless of use case. Hence, whether asking
for bare metal access, virtual machine access, or use of default images,
the charge is the same --- you are charged for the fraction of the
resource your experiment occupies, regardless of the type of the
experiment.

The basic principle for charging service units for Chameleon resources
is to evaluate the amount of time a fraction of the resource is
unavailable to other users. If a reservation is made through the portal
for a particular date/time in the future, the user will be charged for
this time regardless of whether the reservation is actually used, as the
Chameleon scheduling system will have to drain the appropriate part of
the system to satisfy the reservation, even if the nodes requested are
not actually used. A reservation request may be cancelled in which case
no charges will apply.

## Project Allocation Size

Currently Chameleon is operating on a "soft allocation model" where each
project, if approved, will receive a startup allocation of 20,000 SUs
for six months that can be both recharged (i.e., more SUs can be added)
and renewed (i.e., the duration can be extended) via submitting a
renew/recharge request. This startup allocation value has been designed
to respond to both PI needs (i.e., cover an amount of experimentation
needed to obtain a significant result) and balance fairness to other
users (it represents roughly 1% of testbed six months' capacity).
Requests for these startup projects will receive a fast track internal
review (i.e., users can expect them to be approved within a few days).

A PI can apply for multiple projects/allocations; however, the number of
held allocations will be taken into account during review.

As our understanding of user need grows we expect the Chameleon
allocation model to evolve towards closer reflection of those needs in
the form of more differentiated allocations that will allow us to give
larger allocations to users for longer time.

Please be mindful to shutting down your VMS when not in use as even VMs
that do not do any calculations get charged. In past classes we had
students that did not shut down their VMs and within 2 weeks used up all
SUs for the entire class of 70 students. We like to avoid this. In
future cases we will assign the grade "F" to such students, as is
customary also in other universities.
