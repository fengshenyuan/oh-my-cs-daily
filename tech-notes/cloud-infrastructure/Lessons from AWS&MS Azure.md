# Lessons from AWS & MS Azure

AWS Jeff Bezos 2002
* All teams will henceforth expose their data and functionality through service interfaces.
* Teams must communicate with each other through these interfaces.
* There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another team’s data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network.
* It doesn’t matter what technology they use. HTTP, Corba, Pubsub, custom protocols — doesn’t matter.
* All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.
* Anyone who doesn’t do this will be fired.
