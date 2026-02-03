Proposal: GFNS Tag Vocabulary
=============================

Current Rule
------------

The `Tag Vocabulary codelist <https://iatistandard.org/en/iati-standard/203/codelists/tagvocabulary/>`_ has 4 named values and a single “meta” value

Proposed Change
---------------

Add a new code to the Tag Vocabulary codelist: 5 for `Global Food and Nutrition Security (GFNS) <https://www.gafs.info>`_. 

Use of an ISO 2-letter country code alongside this vocabulary indicates that the activity relates to a GFNS Preparedness Plan. 

Rationale
---------

Activation by a country’s government of a Global Food and Nutrition Security (GFNS) Preparedness Plan (PP) results in the rapid deployment of resources in a pre-agreed manner to address a situation quickly and efficiently.

When a PP is activated, it is important that the response from donors can be quickly identified, and distinguished from unrelated Food & Nutrition Security (FNS) activity.

IATI data contains much of the necessary information for tracking response to PP activation, and can be published and updated quickly.  

However, the IATI Standard lacks a way of differentiating between a specific PP activation response and other work to address FNS issues that may be ongoing.

The addition of a specific vocabulary enables activities that are wholly or partly associated with a PP activation to be consistently and unambiguously identified.  

By adding this vocabulary to IATI, existing data infrastructure can be leveraged for this new and impactful application as well as contributing valuable data to the wider IATI corpus. 


Impact
------

Those responding to Global Food and Nutrition Security (GFNS) Preparedness Plan activations will be able to use IATI data to annotate and flag relevant activities.  

No data will become invalid as a result of this change. 

Data publication and use systems will need to add the new code only if required to publish or use data that includes it. Other systems should be unaffected. 

Tools that use the tag vocabulary codelist (eg d-portal, IATI Datastore) will update, to enable users to filter IATI data for this.

As of 18th January 2026, no published data uses the proposed new code, so the risk of accidental use of the new code is negligible. 


Principles Assessment
---------------------

+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Principle                                                                | Assessment                                                       |    |
+==========================================================================+==================================================================+====+
| Increase Simplicity to ensure ease of use                                | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve Conceptual Alignment to ensure intuitive understanding.          | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase Modularity so that concepts can be separated                    | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase the Precision of the Standard                                   | Creates a new application of the Standard without introducing    | ✅ |
|                                                                          | new data structures.                                             |   |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve the Integrity & coherence of the Standard                        | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Integrate the expectation of Change so that the Standard can continue to | Demonstrates IATI's responsiveness to changing requirements      | ✅ |
| evolve                                                                   |                                                                  |   |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+

Source Materials & Evidence
---------------------------

IATI has a long-running strategic partnership with GFNS in order to advance our shared mission. This change has been developed through collaboration between both organisations and in consultation with organisations that will be responding to PP activations. 

To support usage of this code, `implementation documentation <https://gfns-reporting.iatistandard.org/en/latest/>`_ has been prepared.

Change Details
--------------

See `this GitHub Pull Request <https://github.com/IATI/IATI-Codelists-NonEmbedded/pull/434>`_ for the specific changes proposed. 


Implementation
--------------

The IATI Standard will be updated on GitHub immediately after the 30 day proposal period ends; the IATI website will be updated within a few days. 

IATI Secretariat-maintained tools will be updated during their usual maintenance cycles, which are over several months. 


Participation
-------------

You can contribute in English, French or Spanish. The Secretariat and the IATI community will use machine translation to read your contribution and respond. 

If you have a GitHub account, you can comment on the pull request. Please start your comment with the words:

**SUPPORT** - if this proposal is something that you wish to see proceed

**QUESTION** - if you require more information to form a view on the proposal

**CONCERN** - if this proposal concerns you and you would like to see a revision or amendment

**OBJECTION** - if you object to this proposal proceeding

The IATI Secretariat will read all responses and find a way to proceed. 

If you do not have a GitHub account, you can `contact the IATI Secretariat <https://iatistandard.org/en/guidance/get-support/>`_ to voice your views; the Secretariat will post a summary of the conversation on GitHub for transparency. 

Alternatively, you can start a discussion on IATI Connect. The IATI Secretariat will read and respond appropriately, and post a summary of the conversation on GitHub for transparency. 

