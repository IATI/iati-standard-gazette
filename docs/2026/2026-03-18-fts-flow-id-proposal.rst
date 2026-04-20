Proposal: Add FTS Flow ID to other-identifier-code
==================================================

.. note::

    This proposal was circulated in the 2026-03-18 edition of the IATI Standard Gazette.

    No objections were received, and the proposal passed on 2026-04-17. 
    The proposed changes were `merged <https://github.com/IATI/IATI-Codelists-NonEmbedded/pull/435>`_ on 2026-04-20. 


Current Rule
------------

The `Other Identifier Type <https://iatistandard.org/en/iati-standard/203/codelists/otheridentifiertype/>`_ codelist contains three codes to describe different kinds of identifier that may refer to the same activity: one for a reporting org's internal ID, one for a CRS ID, and one for a previous IATI activity-id. There is also one catch-all code, for any other identifier. 

Proposed Change
---------------

That a fourth code be added to the list, for an FTS Flow ID that refers to the same activity as the IATI activity. 

Rationale
---------

Many organisations that support humanitarian work report to both UN-OCHA's `Financial Tracking Service (FTS) <https://fts.unocha.org/>`_ and IATI; providing a way to link between the two means that a data user can be assured that an FTS flow and an IATI activity do, in fact, refer to the same funding. FTS and IATI have different scopes; combining data from both allows for a more well-rounded analysis to be conducted. 

Impact
------

Adding a new code to an existing non-core codelist has no impact on validation status. IATI tools will not need to be updated except to support the new code in filters. 

Neither publishers nor data users will need to change existing routines as a direct result of this change. 

Organisations that publish to both IATI and FTS will be able to publish a new value that creates a connection between the publicly available data across IATI and FTS. Organisations whose IATI data is suitably structured may be able automate their FTS reporting from their IATI data using this new value. 

Users of IATI, in particular creators of dashboards and data analysis tools, will be able to incorporate IATI and FTS data more easily into their analysis. 

Approximately 1/3 IATI activities are flagged as humanitarian, so the potential value is substantial. 

Principles Assessment
---------------------


+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Principle                                                                | Assessment                                                       |    |
+==========================================================================+==================================================================+====+
| Increase Simplicity to ensure ease of use                                | Using an existing codelist to add new functionality              | ✅ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve Conceptual Alignment to ensure intuitive understanding.          | Ensures that organisations that report to FTS as well can more   | ✅ |
|                                                                          | richly describe their work                                       |    |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase Modularity so that concepts can be separated                    | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase the Precision of the Standard                                   | Where an organisation's humanitarian work is aligned with FTS    | ✅ |
|                                                                          | definitions this can be communicated                             |    |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve the Integrity & coherence of the Standard                        | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Integrate the expectation of Change so that the Standard can continue to | A potentially impactful change with minimal external effects     | ✅ |
| evolve                                                                   |                                                                  |    |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+

Source Materials & Evidence
---------------------------

During 2025, Denmark's Ministry of Foreign Affairs carried out a pilot project using their IATI publication to create their FTS reporting submissions. This was successful, and this proposal supports wider adoption of this practice. 

Change Details
--------------

A new code, A4, will be added to the `Other Identifier Type <https://iatistandard.org/en/iati-standard/203/codelists/otheridentifiertype/>`_ codelist with name "FTS Flow ID" and description "Identifier assigned by UN-OCHA once the flow has been curated and published in FTS"

See `this GitHub Pull Request <https://github.com/IATI/IATI-Codelists-NonEmbedded/pull/435>`_ for details. 

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

Alternatively, you can start a discussion on `IATI Connect <https://iaticonnect.org>`_. The IATI Secretariat will read and respond appropriately, and post a summary of the conversation on GitHub for transparency. 