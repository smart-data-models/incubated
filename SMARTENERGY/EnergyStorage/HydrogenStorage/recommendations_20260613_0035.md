# Smart Data Models — Review Report: HydrogenStorage

**Date:** 2026-06-13 00:35 UTC
**Schema version:** 0.0.1
**Model path:** incubated/SMARTENERGY/EnergyStorage/HydrogenStorage
**Status:** ✅ READY FOR PUBLICATION

All 12 validation tests passed. Corrected files have been committed to the incubated
repository and a publication request has been sent to alberto.abella@transparentia.net.

---

## Test Results

| Test | Result |
|------|--------|
| test_file_exists | ✅ PASS |
| test_valid_json | ✅ PASS |
| test_yaml_files | ✅ PASS |
| test_schema_descriptions | ✅ PASS |
| test_schema_metadata | ⚠️ WARN |
| test_string_incorrect | ✅ PASS |
| test_valid_keyvalues_examples | ✅ PASS |
| test_valid_ngsiv2 | ✅ PASS |
| test_valid_ngsild | ✅ PASS |
| test_duplicated_attributes | ✅ PASS |
| test_array_object_structure | ✅ PASS |
| test_name_attributes | ✅ PASS |

---

## Auto-generated Files Removed

None

---

## Auto-fixes Applied

- **[Fix A]** Updated `$schema` from `http://json-schema.org/schema#` to `https://json-schema.org/draft/2020-12/schema`
- **[Fix A]** Removed trailing comma from `$id` value
- **[Fix A]** Expanded `description` to meet 50-character minimum: `"A generic tank used for storing compressed hydrogen gas at high pressure"`
- **[Fix C]** Added missing descriptions to `location.type`, `location.coordinates`, and `location.coordinates.items`
- **[Fix]** Generated missing `example.jsonld` (key-values format with `@context`)
- **[Fix]** Generated missing `example-normalized.json` (NGSIv2 normalized format)
- **[Fix]** Generated missing `example-normalized.jsonld` (NGSI-LD normalized format)

---

## Warnings (non-blocking)

- test_schema_metadata: `$id` URL not yet reachable — expected for unpublished model

---

## Contribution Agreement Reminder
⚠️ Please ensure the contributor has signed the Smart Data Models Contribution Agreement
before publication is finalised:
https://smartdatamodels.org/index.php/contributor-agreement/
