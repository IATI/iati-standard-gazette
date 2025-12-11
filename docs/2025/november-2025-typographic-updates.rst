Proposal: November 2025 Typographic Updates
==========================================


.. note::

   This proposal was circulated in the 2025-11-10 edition of the IATI Standard Gazette.
   
   No objections were received, and the proposal passed on 2025-12-10. 
   The proposed changes were `merged <https://github.com/IATI/IATI-Schemas/pull/527>`_ on 2025-12-11. 

Current State of Standard
--------------------------

The IATI Standard schema contains a number of typographical errors and inconsistencies. 

Proposed Change
---------------

To correct these errors and inconsistencies while making the minimum possible change to the text and ensuring no change in meaning.

Rationale
---------

Inconsistencies and typographical errors make it harder for someone to understand the Standard, especially if they are new to working with a data standard such as IATI. When the Standard uses different language in two cases, it should be to indicate that there is some kind of difference in the concept that the text refers to; for example if we refer to a "datetime" in one case and a "date-time stamp" in another, a reader may be confused as to whether this difference in wording means that there should be a difference in the data. 

Such issues also make translation harder. 

Impact
------

No data will change validation status as a result of this change.  These changes have no impact on how data is validated by the IATI schema and rulesets.

No published (or to be published) data will be affected by these changes, as they are centred on fixing typographies in the schema.  This will not mean any change to published data. 

These changes do not affect any data publication or tooling. Others that use the IATI schema directly in their systems or processes may choose to bring in the latest version of the schema, but this is not required.

The IATI Standard documentation will update when these changes are implemented.  Any other documentation that uses text from the Standard may need to be updated, but if this doesn't happen then there are no adverse effects; the benefit is just not felt as widely. 

New and existing users of the Standard will find it easier to understand the requirements of the Standard. 

This allows the Secretariat to proceed with engaging translators for the Standard. 

Principles Assessment
---------------------

+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Principle                                                                | Assessment                                                   |      |
+==========================================================================+==============================================================+======+
| Increase Simplicity to ensure ease of use                                | Reducing variance and clarifying text makes the Standard     |      |
|                                                                          | simpler                                                      |  ✅  |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Improve Conceptual Alignment to ensure intuitive understanding.          | No changes to conceptual modelling or meanings of            |  ↔️  |
|                                                                          | descriptions                                                 |      |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Increase Modularity so that concepts can be separated                    | No changes that affect modularity                            |  ↔️  |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Increase the Precision of the Standard                                   | Replacement language is more precise                         |  ✅  |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Improve the Integrity & coherence of the Standard                        | Unnecessary differences are removed                          |  ✅  |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+
| Integrate the expectation of Change so that the Standard can continue to | No changes that affect the expectation of change             |  ↔️  |
| evolve                                                                   |                                                              |      |
+--------------------------------------------------------------------------+--------------------------------------------------------------+------+

Source Materials & Evidence
---------------------------

A number of inconsistencies were identified by IATI Secretariat staff during a review of the schema. These are detailed in `GitHub Issues <https://github.com/IATI/IATI-Schemas/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22November%202025%20Typographic%20Updates%22>`_.


Change Details
--------------

A number of terms that were previously inconsistent will be made consistent. Specifically:

* "IATI Specification" and "IATI Standard" become "IATI Standard" in all cases
* When referring to a date-time, using the phrase "date/time"
* Where a boolean is used as a flag, it is referred to consistently as a "flag" without any modifiers. Other booleans have their descriptions clarified. 

Where psuedocode is used to demonstrate logic in the Standard, its formatting has been changed to include more line breaks to improve clarity.

A typo in the description of :iati-reference:`provider-activity-id` has been resolved

The descriptions of the :iati-reference:`@vocabulary-uri` and :iati-reference:`@version` attributes have been improved for clarity. 

Full details of the proposed changes to the schema can be found at https://github.com/IATI/IATI-Schemas/pull/527

Participation
-------------

You can contribute in English, French or Spanish. The Secretariat and the IATI community will use machine translation to read your contribution and respond. 

If you have a GitHub account, you can comment on the pull request. Please start your comment with the words:

**SUPPORT** - if this proposal is something that you wish to see proceed

**QUESTION** - if you require more information to form a view on the proposal

**CONCERN** - if this proposal concerns you and you would like to see a revision or amendment

**OBJECTION** - if you object to this proposal proceeding

The IATI Secretariat will read all responses and find a way to proceed. 

If you do not have a GitHub account, you can `contact IATI Support <https://iatistandard.org/en/guidance/get-support/>`_ to voice your views; the Secretariat will post a summary of the conversation on GitHub for transparency. 

Alternatively, you can start a discussion on `IATI Connect <https://www.iaticonnect.org>`_. The IATI Secretariat will read and respond appropriately, and post a summary of the conversation on GitHub for transparency. 



