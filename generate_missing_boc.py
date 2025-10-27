#!/usr/bin/env python3
"""Generate comprehensive BOC category content with all HCPCS codes."""

# Complete BOC category mapping with ALL HCPCS codes
BOC_CATEGORIES = {
    "DM02": {
        "name": "DIABETIC EQUIPMENT & SUPPLIES",
        "products": [
            {
                "name": "Blood Glucose Monitor",
                "hcpcs": "E0607",
                "icd10": "E11.9 (Type 2 diabetes), E10.9 (Type 1 diabetes), E11.65 (Hyperglycemia)",
                "indications": "Diabetes mellitus requiring glucose monitoring; insulin-dependent or non-insulin dependent diabetes",
                "necessity": "Diabetes diagnosis; physician order; frequency of testing; training documentation"
            },
            {
                "name": "Continuous Glucose Monitor (CGM)",
                "hcpcs": "E2103",
                "icd10": "E10.65, E11.65, E13.65 (Diabetes with hyperglycemia)",
                "indications": "Type 1 or insulin-treated Type 2 diabetes; frequent hypoglycemia; hypoglycemia unawareness",
                "necessity": "CGM criteria met; insulin use 3+ times daily; 4+ glucose checks daily; therapeutic CGM use"
            },
            {
                "name": "Insulin Infusion Pump",
                "hcpcs": "E0784",
                "icd10": "E10.9, E11.9, E10.10, E10.65",
                "indications": "Type 1 diabetes; insulin-dependent Type 2 diabetes; gastroparesis; dawn phenomenon",
                "necessity": "Insulin pump training; failed MDI therapy; C-peptide levels if Type 2; endocrinologist management"
            },
            {
                "name": "Insulin Infusion Pump - External",
                "hcpcs": "E0784",
                "icd10": "E10.9 (Type 1 DM), E11.9 (Type 2 DM)",
                "indications": "Insulin-dependent diabetes requiring continuous subcutaneous insulin infusion",
                "necessity": "Pump training completed; failed MDI; endocrinology consult"
            }
        ]
    },

    "DM05": {
        "name": "SAFETY EQUIPMENT - PELVIC & EXTREMITY TRACTION",
        "products": [
            {
                "name": "Pelvic Traction Equipment",
                "hcpcs": "E0890, E0900",
                "icd10": "M54.5 (Low back pain), M51.36 (Lumbar disc disorder), M43.16 (Spondylolisthesis)",
                "indications": "Lumbar radiculopathy; disc herniation; muscle spasm; degenerative disc disease",
                "necessity": "Failed conservative therapy; PT prescription; home use justification; trial period results"
            },
            {
                "name": "Cervical Traction Equipment",
                "hcpcs": "E0855, E0856",
                "icd10": "M50.12 (Cervical disc disorder with radiculopathy), M47.22 (Cervical spondylosis with radiculopathy)",
                "indications": "Cervical radiculopathy; disc herniation; nerve root compression; muscle spasm",
                "necessity": "Imaging confirmation; PT prescription; failed other conservative treatments; home safety assessment"
            },
            {
                "name": "Extremity Traction Equipment",
                "hcpcs": "E0870, E0880",
                "icd10": "S72.0 (Femoral neck fracture), S82.0 (Patella fracture), M25.50 (Joint pain)",
                "indications": "Fracture management; joint contracture prevention; post-surgical immobilization",
                "necessity": "Physician order with specific traction parameters; duration; weight specifications"
            }
        ]
    },

    "DM06": {
        "name": "HOSPITAL BEDS & ACCESSORIES",
        "products": [
            {
                "name": "Semi-Electric Hospital Bed",
                "hcpcs": "E0260, E0261",
                "icd10": "M62.81 (Muscle weakness), I50.9 (CHF), J44.1 (COPD), R26.2 (Difficulty walking)",
                "indications": "Severe mobility limitation; cannot safely transfer from standard bed; medical positioning needs",
                "necessity": "Mobility limitation documentation; unsafe with standard bed; positioning requirements; physician face-to-face"
            },
            {
                "name": "Full-Electric Hospital Bed",
                "hcpcs": "E0265, E0266",
                "icd10": "G82.20 (Paraplegia), M62.81, I50.9, J96.10 (Respiratory failure)",
                "indications": "Complete mobility impairment; requires frequent position changes; caregiver limitations",
                "necessity": "Document why semi-electric insufficient; complete immobility; caregiver physical limitations; positioning frequency"
            },
            {
                "name": "Hospital Bed - Heavy Duty",
                "hcpcs": "E0302, E0303, E0304",
                "icd10": "E66.01 (Morbid obesity), M62.81, I50.9",
                "indications": "Patient weight >350 lbs; standard bed inadequate; bariatric patient with mobility limitation",
                "necessity": "Patient weight documentation; medical necessity for bed; standard bed insufficient"
            },
            {
                "name": "Hospital Bed Mattress - Innerspring",
                "hcpcs": "E0271",
                "icd10": "L89.x (Pressure ulcer), M62.81",
                "indications": "Hospital bed use; pressure redistribution; comfort for immobile patient",
                "necessity": "Hospital bed documentation; mattress medical necessity"
            },
            {
                "name": "Hospital Bed Mattress - Foam Rubber",
                "hcpcs": "E0272",
                "icd10": "L89.x, M62.81, G82.20",
                "indications": "Pressure ulcer prevention; immobility; hospital bed use",
                "necessity": "Hospital bed; pressure ulcer risk factors; Braden scale if available"
            },
            {
                "name": "Bed Rails - Full Length",
                "hcpcs": "E0305",
                "icd10": "R26.81 (Unsteadiness), R41.0 (Disorientation), F03.90 (Dementia), R29.6 (Falls)",
                "indications": "Fall risk; confusion; needs repositioning assistance; safety during sleep",
                "necessity": "Fall risk assessment; hospital bed documentation; safety necessity; least restrictive option"
            },
            {
                "name": "Bed Rails - Half Length",
                "hcpcs": "E0310",
                "icd10": "R26.81, M62.81, R29.6",
                "indications": "Moderate fall risk; needs positioning aid; transfer assistance",
                "necessity": "Fall risk; bed rail necessity; why full rails not needed"
            },
            {
                "name": "Trapeze Bar (Bed Attachment)",
                "hcpcs": "E0910, E0911, E0912",
                "icd10": "M62.81, G82.20, Z96.641 (Hip replacement status)",
                "indications": "Needs upper extremity assist for repositioning; post-surgical mobility; strengthening",
                "necessity": "Repositioning needs; upper extremity function adequate; PT recommendation"
            }
        ]
    },

    "DM08": {
        "name": "COMMODE CHAIRS",
        "products": [
            {
                "name": "Bedside Commode - Standard",
                "hcpcs": "E0163 (Fixed arms), E0165 (Detachable arms)",
                "icd10": "R26.2 (Walking difficulty), M62.81 (Muscle weakness), I50.9 (CHF)",
                "indications": "Cannot safely ambulate to bathroom; bedbound or near-bedbound; severe mobility limitation",
                "necessity": "Ambulation limitation; distance to bathroom; fall risk; nighttime safety; physician order"
            },
            {
                "name": "Bedside Commode - Drop-Arm",
                "hcpcs": "E0168",
                "icd10": "R26.2, M62.81, G81.x (Hemiplegia)",
                "indications": "Requires lateral transfer; one-sided weakness; cannot step over standard commode arms",
                "necessity": "Document why standard insufficient; transfer method; one-sided weakness; PT assessment"
            },
            {
                "name": "Bedside Commode - Bariatric",
                "hcpcs": "E0171, E0172",
                "icd10": "E66.01 (Morbid obesity), R26.2, M62.81",
                "indications": "Patient weight >350 lbs (E0171) or >450 lbs (E0172); standard commode inadequate",
                "necessity": "Patient weight; mobility limitation; standard commode insufficient"
            }
        ]
    },

    "DM11": {
        "name": "IPPB (INTERMITTENT POSITIVE PRESSURE BREATHING) MACHINES",
        "products": [
            {
                "name": "IPPB Machine",
                "hcpcs": "E0500",
                "icd10": "J44.1 (COPD with exacerbation), J98.4 (Other lung disorders), J96.10 (Respiratory failure)",
                "indications": "Severe respiratory disease; inability to deep breathe; atelectasis prevention; ineffective cough",
                "necessity": "Pulmonary function tests; failed incentive spirometry; physician documentation of medical necessity; respiratory therapy evaluation"
            },
            {
                "name": "IPPB Replacement Parts",
                "hcpcs": "E0560, E0561, E0562, E0565",
                "icd10": "J44.1, J96.10, J98.4",
                "indications": "Ongoing IPPB therapy; equipment maintenance",
                "necessity": "Current IPPB use documentation; replacement part medical necessity"
            }
        ]
    },

    "DM13": {
        "name": "PATIENT LIFTS",
        "products": [
            {
                "name": "Hydraulic Patient Lift",
                "hcpcs": "E0630",
                "icd10": "M62.81, G82.20 (Paraplegia), G80.9 (Cerebral palsy), R26.2",
                "indications": "Cannot bear weight; caregiver cannot safely transfer patient; complete transfer dependence",
                "necessity": "Patient weight; caregiver physical limitations; transfer dependence; unsafe without lift; home assessment"
            },
            {
                "name": "Electric Patient Lift",
                "hcpcs": "E0635",
                "icd10": "M62.81, G82.20, G80.9",
                "indications": "Requires patient lift; caregiver unable to operate hydraulic lift; frequent transfers needed",
                "necessity": "Document why hydraulic insufficient; caregiver physical limitation; transfer frequency; medical necessity"
            },
            {
                "name": "Patient Lift Sling or Seat",
                "hcpcs": "E0621, E0625, E0629",
                "icd10": "M62.81, G82.20",
                "indications": "For use with patient lift; specific patient positioning needs",
                "necessity": "Patient lift documentation; sling type medical necessity; patient size/needs"
            },
            {
                "name": "Sit-to-Stand Lift",
                "hcpcs": "E0637, E0638, E0639",
                "icd10": "M62.81, M25.50 (Joint pain), R26.2",
                "indications": "Can partially bear weight; cannot fully transfer independently; caregiver assist needed",
                "necessity": "Partial weight-bearing ability; transfer assistance need; PT evaluation"
            }
        ]
    },

    "DM14": {
        "name": "INTERMITTENT URINARY CATHETERS",
        "products": [
            {
                "name": "Intermittent Urinary Catheter - Straight Tip",
                "hcpcs": "A4351, A4352",
                "icd10": "N31.9 (Neurogenic bladder), N39.0 (UTI), G82.20 (Paraplegia), R33.9 (Retention)",
                "indications": "Neurogenic bladder; urinary retention; incomplete bladder emptying; recurrent UTIs from retention",
                "necessity": "Urodynamic studies or PVR measurements; catheterization frequency; clean technique training; physician order with quantity"
            },
            {
                "name": "Intermittent Catheter - Coudé Tip",
                "hcpcs": "A4353",
                "icd10": "N40.1 (BPH with LUTS), N31.9, R33.9",
                "indications": "Urethral stricture; enlarged prostate; difficulty with straight catheter",
                "necessity": "Document why straight tip insufficient; urological evaluation; specific anatomical need"
            },
            {
                "name": "Intermittent Catheter - Hydrophilic Coated",
                "hcpcs": "A4353",
                "icd10": "N31.9, G82.20, N39.0",
                "indications": "Recurrent UTIs; urethral trauma with uncoated catheters; long-term catheterization need",
                "necessity": "Failed standard catheters; UTI history; urethral trauma documentation; medical necessity for coating"
            }
        ]
    },

    "DM15": {
        "name": "INFUSION PUMPS - UNCLASSIFIED",
        "products": [
            {
                "name": "Stationary Infusion Pump",
                "hcpcs": "E0779, E0780",
                "icd10": "Z79.2 (Long-term immunotherapy), C00-D49 (Neoplasms), A41.9 (Sepsis)",
                "indications": "Home IV antibiotics; chemotherapy; TPN; continuous medication infusion",
                "necessity": "Medication requiring pump delivery; physician infusion orders; home health coordination; drug incompatible with gravity infusion"
            },
            {
                "name": "Ambulatory Infusion Pump",
                "hcpcs": "E0781, E0782, E0783, E0784, E0785, E0786, E0787",
                "icd10": "Z79.2, C00-D49, K50.0 (Crohn's disease), K51.0 (Ulcerative colitis)",
                "indications": "Home infusion therapy; patient mobility required; continuous subcutaneous/IV medication",
                "necessity": "Ambulatory infusion medical necessity; medication requiring pump; patient mobility needs"
            }
        ]
    },

    "DM16": {
        "name": "NEBULIZERS & COMPRESSORS",
        "products": [
            {
                "name": "Nebulizer - Portable",
                "hcpcs": "E0570",
                "icd10": "J45.x (Asthma), J44.x (COPD), J20.9 (Bronchitis), J18.9 (Pneumonia)",
                "indications": "Asthma; COPD; chronic respiratory disease requiring nebulized medications",
                "necessity": "Respiratory diagnosis; medication requiring nebulization; inhaler ineffective or contraindicated; physician prescription"
            },
            {
                "name": "Nebulizer - Durable",
                "hcpcs": "E0575",
                "icd10": "J45.x, J44.x, J84.9 (Interstitial lung disease)",
                "indications": "Chronic respiratory condition; frequent nebulizer treatments; home therapy",
                "necessity": "Chronic respiratory diagnosis; frequency of treatments; medication orders"
            },
            {
                "name": "Nebulizer - Ultrasonic",
                "hcpcs": "E0580",
                "icd10": "J45.x, E84.0 (Cystic fibrosis), J84.9",
                "indications": "Thick secretions; cystic fibrosis; requires ultrasonic delivery",
                "necessity": "Document why standard nebulizer insufficient; specific medication requirements; pulmonologist recommendation"
            },
            {
                "name": "Compressor with Nebulizer",
                "hcpcs": "E0572",
                "icd10": "J45.x, J44.x, J20.9",
                "indications": "Asthma; COPD; respiratory disease requiring compressor-driven nebulization",
                "necessity": "Respiratory diagnosis; nebulized medication prescription; home use medical necessity"
            }
        ]
    },

    "DM17": {
        "name": "VENTILATORS",
        "products": [
            {
                "name": "Ventilator - Volume/Pressure (Non-Invasive)",
                "hcpcs": "E0465, E0466",
                "icd10": "J96.10 (Respiratory failure), G47.30 (Sleep apnea), G12.21 (ALS), G71.0 (Muscular dystrophy)",
                "indications": "Chronic respiratory failure; neuromuscular disease; sleep-related hypoventilation; ALS",
                "necessity": "PFTs; ABG results; sleep study; pulmonologist evaluation; ventilator settings; failed BiPAP/CPAP"
            },
            {
                "name": "Ventilator - Invasive (Tracheostomy)",
                "hcpcs": "E0467",
                "icd10": "J96.10, G82.51 (Quadriplegia C1-C4), Z93.0 (Tracheostomy status)",
                "indications": "Ventilator-dependent via tracheostomy; chronic respiratory failure; high spinal cord injury",
                "necessity": "Tracheostomy documentation; vent settings; respiratory failure documentation; pulmonology management"
            }
        ]
    },

    "DM18": {
        "name": "SUCTION PUMPS",
        "products": [
            {
                "name": "Suction Pump - Portable",
                "hcpcs": "E0600",
                "icd10": "Z93.0 (Tracheostomy), J95.02 (Trach complications), R09.89 (Excessive secretions)",
                "indications": "Tracheostomy with secretions; inability to clear airway; excessive oral/respiratory secretions",
                "necessity": "Tracheostomy or airway clearance need; secretion management; physician order; frequency of suctioning"
            },
            {
                "name": "Suction Pump - Stationary",
                "hcpcs": "E0601",
                "icd10": "Z93.0, R09.89, J95.02",
                "indications": "Home suction for tracheostomy; bedside suctioning needs; immobile patient",
                "necessity": "Suctioning medical necessity; stationary use justification; home setup"
            }
        ]
    },

    "DM22": {
        "name": "LYMPHEDEMA PUMPS - SEGMENTAL & NON-SEGMENTAL",
        "products": [
            {
                "name": "Pneumatic Compressor - Non-Segmental",
                "hcpcs": "E0650, E0655",
                "icd10": "I89.0 (Lymphedema), I97.2 (Post-mastectomy lymphedema), I87.2 (Venous insufficiency)",
                "indications": "Lymphedema Stage 2-3; failed conservative therapy; post-surgical lymphedema",
                "necessity": "Lymphedema diagnosis with staging; 4-6 weeks conservative therapy trial; limb measurements; physician order"
            },
            {
                "name": "Pneumatic Compressor - Segmental (4+ chambers)",
                "hcpcs": "E0651, E0652, E0656, E0657, E0660, E0665, E0666, E0667, E0668, E0669, E0670, E0671, E0672, E0673, E0674, E0675, E0676",
                "icd10": "I89.0, I97.2, I87.2",
                "indications": "Stage 2-3 lymphedema; failed non-segmental pump; complex lymphedema",
                "necessity": "Document why non-segmental insufficient; lymphedema severity; compression garment compliance; segmental pump medical necessity"
            }
        ]
    },

    "DM28": {
        "name": "CPAP/BiPAP & RESPIRATORY ASSIST DEVICES",
        "products": [
            {
                "name": "CPAP Device",
                "hcpcs": "E0601",
                "icd10": "G47.33 (Obstructive sleep apnea)",
                "indications": "Obstructive sleep apnea; AHI ≥15 or AHI ≥5 with symptoms",
                "necessity": "Sleep study showing AHI ≥15 OR AHI ≥5 with daytime sleepiness/hypertension/CVD; physician order; mask fitting"
            },
            {
                "name": "BiPAP Device (without backup rate)",
                "hcpcs": "E0470",
                "icd10": "G47.33, J96.10 (Respiratory failure), J44.1 (COPD)",
                "indications": "OSA failing CPAP; restrictive lung disease; obesity hypoventilation; COPD with hypercapnia",
                "necessity": "Failed CPAP trial OR complex sleep apnea OR hypoventilation with CO2 >45; sleep study; ABG if applicable"
            },
            {
                "name": "BiPAP Device (with backup rate)",
                "hcpcs": "E0471",
                "icd10": "J96.10, G47.30 (Central sleep apnea), G12.21 (ALS)",
                "indications": "Central sleep apnea; Cheyne-Stokes; neuromuscular disease; chronic respiratory failure",
                "necessity": "Sleep study showing central apneas OR respiratory failure with hypoventilation; backup rate medical necessity; ABG results"
            },
            {
                "name": "RAD (Respiratory Assist Device)",
                "hcpcs": "E0464",
                "icd10": "G12.21, G71.0 (Muscular dystrophy), J96.10",
                "indications": "Neuromuscular disease with respiratory insufficiency; restrictive thoracic disease",
                "necessity": "PFTs showing restriction; ABG with hypercapnia; neurology/pulmonology consult; specific ventilator settings"
            },
            {
                "name": "CPAP/BiPAP Heated Humidifier",
                "hcpcs": "E0562",
                "icd10": "G47.33, J96.10",
                "indications": "Dryness/discomfort with CPAP/BiPAP; nasal congestion; compliance issues from dryness",
                "necessity": "CPAP/BiPAP use; dryness symptoms; compliance enhancement; physician order"
            }
        ]
    },

    "M01": {
        "name": "CANES",
        "products": [
            {
                "name": "Cane - Single Point",
                "hcpcs": "E0100",
                "icd10": "R26.81 (Unsteadiness), M25.50 (Joint pain), R26.2 (Difficulty walking)",
                "indications": "Mild balance impairment; unilateral weakness; gait instability; joint pain affecting ambulation",
                "necessity": "Gait instability; balance impairment; physician/PT order; single point adequate for needs"
            },
            {
                "name": "Cane - Quad/3-Point",
                "hcpcs": "E0105",
                "icd10": "R26.81, G81.x (Hemiplegia), I69.x (Stroke sequelae)",
                "indications": "Moderate balance impairment; hemiplegia; stroke; needs more stability than single point",
                "necessity": "Document why single-point insufficient; balance impairment severity; PT evaluation"
            },
            {
                "name": "Walk-Easy Cane",
                "hcpcs": "E0110",
                "icd10": "R26.81, M25.50, G20 (Parkinson's)",
                "indications": "Severe balance impairment; Parkinson's disease; needs maximum cane stability",
                "necessity": "Document why quad cane insufficient; specific disease process; PT recommendation"
            }
        ]
    },

    "M05": {
        "name": "CRUTCHES",
        "products": [
            {
                "name": "Crutches - Forearm (Pair)",
                "hcpcs": "E0110, E0111",
                "icd10": "S82.0 (Fracture lower leg), S92.0 (Fracture foot), M25.561 (Knee pain)",
                "indications": "Non-weight bearing or partial weight bearing on lower extremity; post-surgical; fracture",
                "necessity": "Weight-bearing restriction; physician order specifying restrictions; duration; PT training"
            },
            {
                "name": "Crutches - Underarm (Pair)",
                "hcpcs": "E0112, E0113, E0114",
                "icd10": "S82.0, S92.0, M25.561, Z96.641 (Post joint replacement)",
                "indications": "Temporary non-weight bearing or partial weight bearing; post-surgical; injury",
                "necessity": "Weight-bearing orders; expected duration; crutch gait training; physician order"
            }
        ]
    },

    "M06A": {
        "name": "POWER SCOOTERS",
        "products": [
            {
                "name": "Power Scooter - Class 2 (3-Wheel)",
                "hcpcs": "K0800, K0801, K0802",
                "icd10": "M62.81, G82.20, M17.0 (Knee OA), I73.9 (PVD), J44.1 (COPD)",
                "indications": "Cannot safely use manual wheelchair; can transfer independently; adequate upper extremity function; limited ambulation",
                "necessity": "Mobility limitation in home; cannot use manual WC; safe transfer ability; adequate vision/cognition; face-to-face exam; home assessment"
            },
            {
                "name": "Power Scooter - Class 2 (4-Wheel)",
                "hcpcs": "K0806, K0807, K0808",
                "icd10": "M62.81, G82.20, M17.0, I73.9",
                "indications": "Same as 3-wheel but needs additional stability; outdoor use; uneven terrain",
                "necessity": "Scooter medical necessity; document why 3-wheel insufficient; stability needs; usage environment"
            },
            {
                "name": "Power Scooter - Heavy Duty",
                "hcpcs": "K0809, K0810, K0811, K0812, K0813, K0814",
                "icd10": "E66.01 (Morbid obesity), M62.81, G82.20",
                "indications": "Standard scooter weight capacity insufficient; patient >300 lbs",
                "necessity": "Patient weight; standard scooter insufficient; mobility limitation; medical necessity"
            }
        ]
    },

    "M07": {
        "name": "MANUAL WHEELCHAIR ACCESSORIES",
        "products": [
            {
                "name": "Manual Wheelchair Anti-Tipping Device",
                "hcpcs": "E0971, E0972",
                "icd10": "R26.81 (Unsteadiness), R29.6 (Falls), G82.20",
                "indications": "Fall risk; wheelchair tipping risk; impaired balance/judgment",
                "necessity": "Fall risk; tipping risk assessment; medical necessity; PT evaluation"
            },
            {
                "name": "Manual Wheelchair Headrest",
                "hcpcs": "E0955, E0956",
                "icd10": "G82.20, G80.9 (Cerebral palsy), M62.81",
                "indications": "Inadequate head/neck control; positioning needs; trunk/neck weakness",
                "necessity": "Head control deficit; positioning medical necessity; PT/OT evaluation"
            },
            {
                "name": "Manual Wheelchair Arm Trough",
                "hcpcs": "E0951, E0952, E0953",
                "icd10": "G81.x (Hemiplegia), I69.x (Stroke), M62.81",
                "indications": "Arm support needed; hemiplegia; stroke; upper extremity weakness/subluxation",
                "necessity": "Upper extremity weakness; subluxation risk; positioning need; OT evaluation"
            },
            {
                "name": "Wheelchair Cushion - General",
                "hcpcs": "E2601, E2602, E2603, E2604, E2605",
                "icd10": "L89.x (Pressure ulcer risk), G82.20, M62.81",
                "indications": "Pressure redistribution; immobility; prolonged wheelchair sitting",
                "necessity": "Sitting time >6 hours/day; pressure ulcer risk factors; Braden scale; PT/OT evaluation"
            }
        ]
    },

    "M07A": {
        "name": "POWER WHEELCHAIR ACCESSORIES",
        "products": [
            {
                "name": "Power Wheelchair Tilt-in-Space Seating",
                "hcpcs": "E1002, E1003",
                "icd10": "L89.x (Pressure ulcer), G82.20, G80.9",
                "indications": "High pressure ulcer risk; inability to reposition; orthostatic hypotension; severe postural issues",
                "necessity": "Pressure ulcer history/risk; cannot independently reposition; medical necessity for tilt; PT/seating evaluation"
            },
            {
                "name": "Power Wheelchair - Recline Feature",
                "hcpcs": "E1004, E1005, E1006, E1007, E1008, E1009, E1010",
                "icd10": "G82.20, L89.x, I95.1 (Orthostatic hypotension)",
                "indications": "Orthostatic hypotension; pressure relief; positioning needs; trunk/hip contractures",
                "necessity": "Medical necessity for recline; conditions requiring position changes; PT evaluation"
            },
            {
                "name": "Power Wheelchair Elevating Leg Rests",
                "hcpcs": "E1010, K0046, K0047",
                "icd10": "I87.2 (Venous insufficiency), I83.0 (Varicose veins), I80.x (Phlebitis/thrombophlebitis)",
                "indications": "Lower extremity edema; venous insufficiency; elevation requirement; knee/hip contractures",
                "necessity": "Edema documentation; vascular studies; elevation medical necessity; PT evaluation"
            },
            {
                "name": "Power Wheelchair Headrest",
                "hcpcs": "E2201, E2202, E2203",
                "icd10": "G82.20, G80.9, M62.81",
                "indications": "Inadequate head control; cervical weakness; positioning needs",
                "necessity": "Head control deficits; cervical weakness documentation; positioning medical necessity; PT/OT evaluation"
            },
            {
                "name": "Power Wheelchair Lateral Trunk Supports",
                "hcpcs": "E2218, E2220, E2221",
                "icd10": "G82.20, G80.9, M41.9 (Scoliosis)",
                "indications": "Trunk control deficit; scoliosis; inadequate lateral stability",
                "necessity": "Trunk control assessment; postural deficit; medical necessity; seating evaluation"
            }
        ]
    },

    "M10": {
        "name": "POWER WHEELCHAIRS",
        "products": [
            {
                "name": "Power Wheelchair - Group 1 Standard",
                "hcpcs": "K0813, K0814, K0815, K0816, K0821, K0822",
                "icd10": "M62.81, G82.20, G20 (Parkinson's), M15.9 (OA)",
                "indications": "Mobility limitation in home; cannot self-propel manual WC; inadequate upper extremity strength/endurance",
                "necessity": "Cannot meet needs with manual WC; mobility limitation documented; face-to-face exam; home assessment; failed manual WC trial"
            },
            {
                "name": "Power Wheelchair - Group 2 Standard",
                "hcpcs": "K0820, K0823, K0824, K0825, K0826, K0827, K0828, K0829",
                "icd10": "G82.20, G80.9, G12.21 (ALS), M62.81",
                "indications": "Needs power seating system or increased performance; standard Group 1 insufficient",
                "necessity": "Document why Group 1 insufficient; specific feature needs; complex seating needs; PT evaluation"
            },
            {
                "name": "Power Wheelchair - Group 3 Heavy Duty",
                "hcpcs": "K0848, K0849, K0850, K0851, K0852, K0853, K0854, K0855, K0856, K0857, K0858, K0859, K0860, K0861, K0862, K0863, K0864",
                "icd10": "E66.01, G82.20, M62.81",
                "indications": "Patient weight >250-300 lbs; standard chair weight capacity insufficient; bariatric needs",
                "necessity": "Patient weight; standard chair insufficient; mobility medical necessity; seating width/depth requirements"
            },
            {
                "name": "Power Wheelchair - Group 4 Multiple Power Options",
                "hcpcs": "K0868, K0869, K0870, K0871",
                "icd10": "G82.20, G80.9, G12.21",
                "indications": "Requires multiple power options (tilt, recline, seat elevation, standing); complex positioning",
                "necessity": "Medical necessity for multiple power features; document each feature need; seating evaluation"
            },
            {
                "name": "Power Wheelchair - Group 5 Pediatric",
                "hcpcs": "K0890, K0891",
                "icd10": "G80.9, G71.0, Q05.x (Spina bifida)",
                "indications": "Pediatric patient with severe mobility limitation; growth accommodation needed",
                "necessity": "Age-appropriate medical necessity; growth features; complex pediatric needs"
            }
        ]
    },

    "OR03": {
        "name": "UROLOGICAL SUPPLIES - EXTERNAL CATHETERS & ACCESSORIES",
        "products": [
            {
                "name": "External Urinary Collection Device (Male)",
                "hcpcs": "A4326, A4327, A4328, A4329, A4330",
                "icd10": "R32 (Urinary incontinence), N39.3, N31.9 (Neurogenic bladder)",
                "indications": "Urinary incontinence; neurogenic bladder; cannot use internal catheter",
                "necessity": "Incontinence documentation; why internal catheter inappropriate; skin integrity; quantity justification"
            },
            {
                "name": "Urinary Drainage Bag (Leg Bag)",
                "hcpcs": "A4357, A4358",
                "icd10": "N39.0, Z93.6 (Catheter status), N31.9",
                "indications": "Indwelling catheter use; urinary retention management; mobility needs",
                "necessity": "Catheter use documentation; bag type medical necessity; quantity per month"
            },
            {
                "name": "Urinary Suspensory/Straps",
                "hcpcs": "A4360",
                "icd10": "Z93.6, N39.0",
                "indications": "Secures leg bag; catheter management",
                "necessity": "Leg bag use; securing device medical necessity"
            }
        ]
    },

    "PD08": {
        "name": "UPPER EXTREMITY PROSTHETICS",
        "products": [
            {
                "name": "Upper Extremity Prosthesis - Partial Hand",
                "hcpcs": "L6000-L6026",
                "icd10": "Z89.0 (Acquired finger absence), Z89.1 (Hand absence), S68.x (Traumatic amputation)",
                "indications": "Partial hand amputation; functional restoration; ADL independence",
                "necessity": "Amputation level documentation; functional goals; prosthetic evaluation; medical necessity for specific components"
            },
            {
                "name": "Upper Extremity Prosthesis - Wrist Disarticulation/Below Elbow",
                "hcpcs": "L6050-L6370",
                "icd10": "Z89.11 (Hand/wrist amputation), S58.x (Forearm amputation)",
                "indications": "Below elbow amputation; functional restoration; work/ADL needs",
                "necessity": "Amputation level; residual limb length; functional goals; prosthetic prescription; componentry justification"
            },
            {
                "name": "Upper Extremity Prosthesis - Elbow Disarticulation/Above Elbow",
                "hcpcs": "L6400-L6570",
                "icd10": "Z89.12 (Arm above elbow amputation), S58.x",
                "indications": "Above elbow amputation; functional needs; prosthetic candidacy",
                "necessity": "Amputation level; medical stability; functional goals; componentry medical necessity"
            },
            {
                "name": "Upper Extremity Prosthesis - Shoulder Disarticulation",
                "hcpcs": "L6550-L6590",
                "icd10": "Z89.13 (Shoulder amputation), S48.x (Shoulder/upper arm amputation)",
                "indications": "Shoulder level amputation; functional restoration goals",
                "necessity": "Amputation level; prosthetic candidacy; functional goals; complex componentry justification"
            },
            {
                "name": "Myoelectric Components (Upper Extremity)",
                "hcpcs": "L6880-L6885, L6920-L6975",
                "icd10": "Z89.x (Amputations), Z44.x (Prosthetic fitting)",
                "indications": "Upper extremity amputation requiring myoelectric control; improved function over body-powered",
                "necessity": "Document why myoelectric needed over body-powered; EMG signals adequate; training potential; functional benefit; cost-benefit analysis"
            }
        ]
    },

    "PD09": {
        "name": "UROLOGICAL SUPPLIES - OSTOMY",
        "products": [
            {
                "name": "Urinary Ostomy Pouch - Drainable",
                "hcpcs": "A4375, A4376, A4377, A4378, A4379, A4380, A4381, A4382, A4383, A4384, A4385, A4386, A4387, A4388, A4389, A4390, A4391",
                "icd10": "Z93.6 (Urostomy status), C67.x (Bladder cancer), N32.81 (Bladder dysfunction)",
                "indications": "Urinary diversion/urostomy; bladder cancer post-cystectomy; neurogenic bladder with diversion",
                "necessity": "Urostomy documentation; surgical report; pouch type/size medical necessity; quantity per month justification"
            },
            {
                "name": "Ostomy Skin Barrier/Wafer",
                "hcpcs": "A4404, A4405, A4406, A4407, A4408, A4409, A4410, A4411, A4412, A4413, A4414, A4415, A4416, A4417, A4418, A4419, A4420, A4421, A4422, A4423, A4424, A4425, A4426, A4427, A4428, A4429, A4430, A4431, A4432, A4433, A4434, A4435",
                "icd10": "Z93.6, Z93.3 (Colostomy), Z93.4 (Ileostomy)",
                "indications": "Ostomy skin protection; barrier between stoma and pouch",
                "necessity": "Ostomy type; stoma size; barrier size/type medical necessity; monthly quantity"
            },
            {
                "name": "Ostomy Belt",
                "hcpcs": "A4367",
                "icd10": "Z93.6, Z93.3, Z93.4",
                "indications": "Secures ostomy pouch; abdominal contour issues; pouch stability",
                "necessity": "Ostomy documentation; belt medical necessity (flush stoma, skin folds, activity level)"
            },
            {
                "name": "Ostomy Pouch Closure/Clamp",
                "hcpcs": "A4363, A4364",
                "icd10": "Z93.6, Z93.3, Z93.4",
                "indications": "Drainable ostomy pouch closure",
                "necessity": "Drainable pouch use; quantity justification"
            }
        ]
    },

    "PE03": {
        "name": "PARAFFIN BATH UNITS",
        "products": [
            {
                "name": "Paraffin Bath Unit",
                "hcpcs": "E0235",
                "icd10": "M15.9 (Osteoarthritis), M79.3 (Panniculitis), M06.9 (Rheumatoid arthritis), I73.00 (Raynaud's)",
                "indications": "Arthritis pain management; joint stiffness; scleroderma; Raynaud's; hand therapy",
                "necessity": "Chronic condition requiring heat therapy; failed other conservative treatments; PT/OT prescription; frequency of use; home therapy medical necessity"
            }
        ]
    },

    "R07": {
        "name": "APNEA MONITORS",
        "products": [
            {
                "name": "Apnea Monitor",
                "hcpcs": "E0618, E0619",
                "icd10": "P28.3 (Primary sleep apnea of newborn), R06.81 (Apnea), P07.x (Prematurity)",
                "indications": "Infant apnea; prematurity with apnea episodes; ALTE (Apparent Life-Threatening Event); high-risk infant",
                "necessity": "Documented apnea episodes; NICU history; pediatric pulmonology/cardiology evaluation; monitor duration; download reports"
            }
        ]
    },

    "S01": {
        "name": "CANES",
        "products": [
            {
                "name": "Cane - Adjustable/Standard",
                "hcpcs": "E0100",
                "icd10": "R26.81 (Unsteadiness), M25.50 (Joint pain), R26.2 (Difficulty walking), G20 (Parkinson's)",
                "indications": "Gait instability; mild balance impairment; unilateral weakness; joint pain affecting ambulation",
                "necessity": "Balance/gait impairment; physician/PT order; medical necessity for ambulation safety"
            },
            {
                "name": "Cane - Quad/Multi-Prong",
                "hcpcs": "E0105",
                "icd10": "R26.81, G81.x (Hemiplegia), I69.x (Stroke sequelae), G20",
                "indications": "Moderate-severe balance impairment; hemiplegia; stroke; single-point cane insufficient",
                "necessity": "Document why single-point insufficient; balance severity; stroke/hemiplegia documentation; PT evaluation"
            },
            {
                "name": "Cane - White (for Blind)",
                "hcpcs": "E0105",
                "icd10": "H54.x (Blindness/low vision)",
                "indications": "Legally blind; visual impairment requiring navigation aid",
                "necessity": "Visual impairment documentation; ophthalmology records; legal blindness certification"
            }
        ]
    },

    "S04": {
        "name": "WALKERS",
        "products": [
            {
                "name": "Walker - Rigid (No Wheels)",
                "hcpcs": "E0130, E0135",
                "icd10": "R26.2, M62.81, R26.81, M25.50",
                "indications": "Significant gait/balance impairment; needs maximum stability; partial weight-bearing",
                "necessity": "Balance/gait deficit; medical necessity for walker; PT evaluation; can lift walker"
            },
            {
                "name": "Walker - Folding (No Wheels)",
                "hcpcs": "E0141, E0143",
                "icd10": "R26.2, M62.81, R26.81",
                "indications": "Same as rigid walker; needs portability/transport capability",
                "necessity": "Walker medical necessity; portability need; can manage folding mechanism"
            },
            {
                "name": "Walker - 2-Wheeled (Front Wheels)",
                "hcpcs": "E0143, E0144",
                "icd10": "R26.2, R26.81, G20 (Parkinson's), M62.81",
                "indications": "Gait impairment; difficulty lifting walker; needs continuous forward motion",
                "necessity": "Document why rigid walker insufficient; cannot safely lift walker; gait pattern requires wheels"
            },
            {
                "name": "Walker - 4-Wheeled (Rollator)",
                "hcpcs": "E0147, E0148, E0149",
                "icd10": "R26.81, M62.81, I50.9 (CHF), J44.1 (COPD)",
                "indications": "Balance impairment with fatigue; endurance limitation; needs seat for rest; COPD/CHF",
                "necessity": "Balance impairment plus endurance limitation; medical necessity for seat; safe brake use; PT evaluation"
            },
            {
                "name": "Walker - Enclosed/4-Sided Frame",
                "hcpcs": "E0144",
                "icd10": "R26.81, G81.x, I69.x, G20",
                "indications": "Severe balance impairment; significant postural instability; needs maximum stability",
                "necessity": "Document why standard walker insufficient; severe instability; fall risk; PT assessment"
            },
            {
                "name": "Walker - Heavy Duty (>300 lbs)",
                "hcpcs": "E0148, E0149",
                "icd10": "E66.01, R26.2, M62.81",
                "indications": "Patient weight >300 lbs; standard walker weight capacity insufficient",
                "necessity": "Patient weight; standard walker insufficient; mobility/balance impairment"
            },
            {
                "name": "Walker Attachments (Platform, Leg Extensions, Wheels, Seats)",
                "hcpcs": "E0153, E0154, E0155, E0156, E0157, E0158, E0159",
                "icd10": "R26.2, M62.81, M25.50",
                "indications": "Specific attachment enhances walker function; upper extremity limitations; height needs",
                "necessity": "Walker use documentation; specific attachment medical necessity; PT recommendation"
            }
        ]
    }
}

def generate_product_html(product):
    """Generate HTML for a single product card."""
    return f'''            <div class="product-card">
                <div class="product-name">{product["name"]}</div>
                <div class="code-row">
                    <div class="code-label">HCPCS:</div>
                    <div class="code-value">{product["hcpcs"]}</div>
                </div>
                <div class="code-row">
                    <div class="code-label">ICD-10:</div>
                    <div class="code-value">{product["icd10"]}</div>
                </div>
                <div class="clinical-box">
                    <strong>INDICATIONS:</strong> {product["indications"]}
                </div>
                <div class="med-necessity">
                    <strong>REQUIRE:</strong> {product["necessity"]}
                </div>
            </div>'''

def generate_category_html(boc_code, category_data):
    """Generate complete HTML section for a BOC category."""
    products_html = '\n'.join([generate_product_html(p) for p in category_data["products"]])

    return f'''
    <!-- {boc_code}: {category_data["name"]} -->
    <div class="category-section">
        <div class="category-header">
            {boc_code}: {category_data["name"]} (BOC Category)
        </div>
        <div class="product-grid">
{products_html}
        </div>
    </div>'''

# Generate all HTML content
all_html = []
for boc_code in sorted(BOC_CATEGORIES.keys()):
    html_section = generate_category_html(boc_code, BOC_CATEGORIES[boc_code])
    all_html.append(html_section)

# Write to output file
output_content = '\n'.join(all_html)

with open('/home/user/ClaudeCatalogRepo/new_boc_sections.html', 'w') as f:
    f.write(output_content)

print(f"✅ Generated {len(BOC_CATEGORIES)} BOC category sections")
print(f"📝 Total products: {sum(len(cat['products']) for cat in BOC_CATEGORIES.values())}")
print(f"💾 Output: /home/user/ClaudeCatalogRepo/new_boc_sections.html")
