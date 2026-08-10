Proposal: Synchronisation with OECD DAC codelists
=================================================

.. note::

   This proposal was circulated in the 2026-06-30 edition of the IATI Standard Gazette.
   No objections were received, and the proposal passed on 2026-07-30. The proposed changes were merged on 2026-08-03.


Current Rule
------------

Several IATI codelists are derived from the OECD DAC codelists. These were last updated on 2023-08-29. Subsequent updates have been delayed because of the work required to update the synchronisation code following changes to the DAC's systems.

Proposed Change
---------------

Update the relevant IATI codelists to the latest OECD DAC version available as of 4 June 2026.

IATI codelists now use the authoritative OECD source (`Development finance classifications <https://development-finance-codelists.oecd.org/Codeslist.aspx>`_) rather than the previously agreed IATI XML version, which is now broadly in line with the IATI XML structure. 

The IATI codelist for Sector to include a flag for CRS or TOSSD.

The following codelists will be updated, in line with the OECD DAC source:

- Aid Type
- CRS Channel
- Finance Type
- Flow Type
- Sector (Purpose Code in source)

Additionally, two IATI codelists which act as category lists will be updated:

- Aid Type category
- Sector category

Rationale
---------

Keeping IATI and OECD DAC codelists in close synchronisation ensures cross-compatibility between IATI, CRS and TOSSD datasets, and enables better harmonisation. Minimising the delay in this synchronisation also reduces possible validation errors and other feedback for publishers.

Impact
------

No data will see its validation status downgraded because of this change; IATI's approach to withdrawn codes is to keep them in the codelist with ``status="withdrawn"`` to ensure that validation is not affected.

Any data that currently uses the codes added by this update will currently have Error status; this update will resolve that.

Many of the changes are to the descriptions of codes, or are updates to category codes. Organisations should review the new descriptions to ensure that they are still using the correct codes: some description changes narrow the scope of codes, or advise the use of alternative codes for specific cases.

For each codelist, a `full analysis <https://deepnote.com/app/Open-Data-Services-Cooperative/DAC-Codes-c42935af-df37-437a-b830-76a25c6049d2>`_ has been prepared, which details:

- where each codelist is used in the IATI Standard;
- the number of reporting organisations using the values that will be updated;
- changed, new and withdrawn codes, where relevant;
- a summary box of the changes.

The same analysis is also provided for the two category lists.

Principles Assessment
---------------------

+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Principle                                                                | Assessment                                                       |    |
+==========================================================================+==================================================================+====+
| Increase Simplicity to ensure ease of use                                | Uses the authoritative OECD source directly                      | ✅ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve Conceptual Alignment to ensure intuitive understanding.          | Brings IATI codes back in line with OECD DAC                     | ✅ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase Modularity so that concepts can be separated                    | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Increase the Precision of the Standard                                   | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Improve the Integrity & coherence of the Standard                        | No change                                                        | ↔️ |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+
| Integrate the expectation of Change so that the Standard can continue to | Restores regular synchronisation with OECD updates               | ✅ |
| evolve                                                                   |                                                                  |    |
+--------------------------------------------------------------------------+------------------------------------------------------------------+----+

Source Materials & Evidence
---------------------------

`Codelist change analysis <https://deepnote.com/app/Open-Data-Services-Cooperative/DAC-Codes-c42935af-df37-437a-b830-76a25c6049d2>`_ (IATI Secretariat)
`Development finance codelists <https://development-finance-codelists.oecd.org/Codeslist.aspx>`_ (OECD DAC) 


Change Details
--------------

See `this GitHub Pull Request <https://github.com/IATI/IATI-Codelists-NonEmbedded/pull/427/>`_ for the specific changes proposed.

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
