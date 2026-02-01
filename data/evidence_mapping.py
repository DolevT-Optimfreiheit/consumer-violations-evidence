# Evidence mapping - connects violations to supporting evidence
from pathlib import Path

# Get evidence directory relative to this file
EVIDENCE_DIR = Path(__file__).parent.parent

# Comprehensive evidence mapping for all 7 violations
EVIDENCE_MAP = {
    "§ 242 BGB - Bad Faith Inducement": {
        "law_code": "§ 242 BGB",
        "title": "Bad Faith Inducement (Venire contra factum proprium)",
        "description": "The merchant contacted the consumer via telephone and insisted that bulk orders were required to qualify for free shipping, explicitly stating that weekly 70L orders would not receive free shipping benefits. Relying on this representation, the consumer placed a 243L bulk order. Subsequently, the merchant demanded an additional €150 surcharge and withheld shipment pending payment. This contradictory conduct—encouraging bulk purchases while simultaneously imposing surcharges on such purchases—constitutes a violation of the good faith principle (§ 242 BGB). Additionally, the merchant engaged in a pattern of repeatedly confirming and subsequently cancelling the same order numbers (e.g., #16142, #16144, #16161, #16245), generating excessive and contradictory communications. The merchant continues to retain consumer funds, with refunds designated as 'upcoming' (e.g., expected 6 February), demonstrating a recurring pattern of fund retention.",
        "evidence": [
            {
                "type": "image",
                "file": "inbox_harassment_confirm_cancel.png",
                "context": "Inbox – confirm/cancel barrage (Jan 2026)",
                "description": "Documentation of repeated confirmations and subsequent cancellations of identical orders (#16142, #16144, #16161, #16245), accompanied by excessive subscription and cart notifications—demonstrating systematic pattern of contradictory communications"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_1.png",
                "context": "Revolut transactions – constant charge/refund pattern (Jan 16-26, 2026)",
                "description": "Documentation of multiple charge and refund transactions: Jan 16 charge -€473.85, Jan 19 refund +€123.20, Jan 24 dual charges -€123.20 ×2 followed by refund +€473.85, with three pending refunds of €123.20 each—demonstrating systematic pattern of financial transactions creating consumer confusion"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_2.png",
                "context": "Revolut transactions – Jan 24 charges and refund (Today view)",
                "description": "Jan 24 transaction sequence: two charges of -€123.20 at 11:02, followed by refund of +€473.85 at 03:40—evidence of systematic charge/refund cycle"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_3.png",
                "context": "Revolut transactions – Jan 25–28 charge/refund cycle (Feb 1, 2026)",
                "description": "Transaction sequence: Jan 25 charge -€123.20 at 11:01; Jan 27 dual refunds +€123.20 ×2 at 15:31; Jan 28 refund +€123.20 at 14:16—demonstrating repeated charge-and-refund pattern"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_4.png",
                "context": "Revolut transactions – Jan 24–25 charges and refund",
                "description": "Transaction sequence: Jan 24 dual charges -€123.20 ×2 at 11:02, refund +€473.85 at 03:40; Jan 25 charge -€123.20 at 11:01—evidence of systematic charging and refunding"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_5.png",
                "context": "Revolut transactions – upcoming refund and Yesterday charge (Feb 1, 2026)",
                "description": "Evidence of fund retention: refund of +€123.20 designated as 'upcoming' with expected date of 6 February—consumer funds being held by merchant; recent charge -€123.20 at 11:02; Jan 28 refund +€123.20—demonstrating recurring pattern of fund retention"
            },
            {
                "type": "call",
                "date": "2026-01-19 13:23",
                "description": "Unanswered phone call - no voicemail, no follow-up",
                "context": "Single call attempt without written response before deadline"
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "Part 1.1 - Coercion to Bulk Orders",
                "lines": "180-182"
            },
            {
                "type": "document",
                "file": "data/eml_extract_default_notice_2026_01_20.md",
                "context": "Declaration of Default (Verzug) – full extract",
                "description": "Full extracted text of ORDER #16045 – 246 LITERS – DECLARATION OF DEFAULT (VERZUG) email (20 Jan 2026), including Annex A (prior WhatsApp communication)."
            },
            {
                "type": "document",
                "file": "data/eml_extract_binding_confirmation_2026_01_22.md",
                "context": "Binding Confirmation – Reinstated Subscription",
                "description": "Full extracted text of Binding Confirmation email (22 Jan 2026); Article V acceptance by performance or written reply."
            }
        ]
    },
    
    "§ 312j BGB - Button Solution Violation": {
        "law_code": "§ 312j BGB",
        "title": "Illegal 'Button Solution' Violation",
        "description": "Section 312j BGB mandates that the total price, including all shipping and delivery charges, must be clearly displayed on the final purchase button before payment authorization. The merchant's shipping policy explicitly states that additional fees are disclosed after order placement, constituting a direct violation of this requirement. Initially, the surcharge clause was positioned in Item 12 at the bottom of the policy in minimal font size. Following receipt of the consumer's formal Default Notice (Verzug declaration with demand for specific performance), the merchant relocated the clause to a more prominent position within the policy. Approximately two weeks after the consumer's last written communication (Binding Confirmation, 22 Jan 2026), the merchant moved Item 12 back down to the bottom of the shipping policy at madeinmarket.eu/policies/shipping-policy—the earlier change was temporary and the practice of placing the clause in minimal prominence has resumed. This revision (and its reversion) fails to remedy the violation: the total price remains absent from the purchase button, and the policy continues to state that additional charges are 'informed after placing order.' Post-payment surcharges remain legally void regardless of policy placement.",
        "evidence": [
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-20 at 14.16.30 (1).jpeg",
                "context": "Terms of Service – hidden surcharge clause",
                "description": "Documentation of shipping policy explicitly stating that additional fees are disclosed after order placement"
            },
            {
                "type": "image",
                "file": "shipping_policy_pre_full_page.png",
                "context": "Shipping Policy – PRE: full page (Item 12 buried in micro-text at bottom)",
                "description": "Documentation of initial policy state: shipping policy with surcharge clause positioned at bottom in minimal font size—Free Shipping tiers prominently displayed, heavy/bulky surcharge clause in minimal text below"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-20 at 15.21.08 (1).jpeg",
                "context": "Shipping Policy - POST: clause moved higher (still 'after placing order')",
                "description": "Documentation of revised policy following receipt of consumer's Default Notice—clause repositioned to more prominent location; however, violation persists as total price remains absent from purchase button and post-payment charges remain legally void"
            },
            {
                "type": "image",
                "file": "shipping_policy_item12_back_down_feb2026.png",
                "context": "Shipping Policy – Item 12 moved back down (Feb 2026)",
                "description": "Approx. two weeks after consumer's last written communication (Binding Confirmation, 22 Jan 2026), merchant moved surcharge clause (Item 12) back to bottom of madeinmarket.eu/policies/shipping-policy—earlier change was temporary; clause again in minimal prominence."
            },
            {
                "type": "image",
                "file": "surcharge proof.PNG",
                "context": "Surcharge proof – Order #16045 (total not on button)",
                "description": "Post-payment surcharge imposed on Order #16045—demonstrates that total price including shipping was not shown on purchase button before payment (§ 312j BGB)."
            },
            {
                "type": "image",
                "file": "surcharge proof smaller order older.PNG",
                "context": "Surcharge proof – smaller/older order (same pattern)",
                "description": "Surcharge applied on earlier order—same pattern: total not disclosed on button, fee demanded after order placement."
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.43.01 (1).jpeg",
                "context": "Order details – surcharge applied after payment (Jan 16)",
                "description": "Order exceeding €99 with additional shipping fee demanded after payment—evidence that final total was not on purchase button."
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.43.39.jpeg",
                "context": "Order breakdown – balance due after payment (Jan 16)",
                "description": "Pricing breakdown showing surcharge and balance due after €473.85 payment—total was not visible on button before click."
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "IV.3 - Illegal Button Solution Violation",
                "lines": "62-68"
            }
        ]
    },
    
    "§ 305c BGB - Surprising Clause": {
        "law_code": "§ 305c BGB",
        "title": "Void 'Surprising Clause' (Überraschende Klauseln)",
        "description": "The surcharge clause was initially positioned in minimal font size at the bottom of the policy (Item 12), rendering it effectively concealed from reasonable consumer review. Following receipt of the consumer's formal Default Notice (Verzug declaration with demand for specific performance), the merchant relocated the clause to a more visible position. Approximately two weeks after the consumer's last written communication (Binding Confirmation, 22 Jan 2026), the merchant moved Item 12 back down to the bottom of the shipping policy—the earlier change was temporary and the practice of placing the clause in minimal prominence has resumed. The revised policy (and its reversion) continues to contradict the 'Free Shipping >€99' representation displayed at checkout, and post-payment surcharges remain legally void. The supplementary clause was not reasonably foreseeable to consumers at the time of contract formation, constituting a violation of § 305c BGB (and Articles 18 and 19 of Portuguese Decree-Law 446/85 regarding unfair contract terms).",
        "evidence": [
            {
                "type": "image",
                "file": "shipping_policy_pre_full_page.png",
                "context": "PRE: Shipping Policy – full page (Item 12 buried in micro-text at bottom)",
                "description": "PRE screenshot: surcharge clause buried at bottom; Free Shipping tiers above, heavy/bulky clause in micro-text – surprising clause under § 305c BGB"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-20 at 15.21.08 (1).jpeg",
                "context": "POST: clause moved higher (still unexpected, still post-payment)",
                "description": "Item 12 – POST more visible only after consumer sent Default Notice (declaration of default + escalation notice); neither PRE nor POST legalizes post-payment charges"
            },
            {
                "type": "image",
                "file": "shipping_policy_item12_back_down_feb2026.png",
                "context": "Shipping Policy – Item 12 moved back down (Feb 2026)",
                "description": "Approx. two weeks after consumer's last written communication (Binding Confirmation, 22 Jan 2026), merchant moved Item 12 back to bottom of shipping policy—earlier change was temporary; clause again in minimal prominence (§ 305c BGB surprising clause)."
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "IV.4 - Void Surprising Clause",
                "lines": "70-77"
            }
        ]
    },
    
    "§ 312a Abs. 3 BGB - Post-Checkout Surcharges": {
        "law_code": "§ 312a Abs. 3 BGB",
        "title": "Illegal Post-Checkout Surcharges",
        "description": "The merchant demanded an additional surcharge exceeding €150 after the consumer had already remitted payment of €473.85. Such post-payment surcharges require express prior consent under § 312a Abs. 3 BGB. No such consent was obtained. This surcharge demand is legally void under both German and Portuguese consumer protection law. Documentary evidence includes order confirmations and payment records demonstrating that the surcharge was imposed after payment completion.",
        "evidence": [
            {
                "type": "pdf",
                "file": "2026-01-16-Order _16045 confirmed.pdf",
                "context": "Order #16045 - Initial payment €473.85",
                "description": "Original order confirmation"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.40.52.jpeg",
                "context": "Post-payment surcharge notice (Jan 16, 00:40)",
                "description": "Documentation of post-payment surcharge demand: additional €150 surcharge imposed after completion of €473.85 payment"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.41.58.jpeg",
                "context": "Payment confirmation – Revolut €473.85 (Jan 16, 00:41)",
                "description": "Proof of full payment on 16 Jan before surcharge demand"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.43.01 (1).jpeg",
                "context": "Order details – surcharge applied (Jan 16, 00:43)",
                "description": "Order exceeding €99 with additional shipping fee demanded after payment"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.43.39.jpeg",
                "context": "Order breakdown – balance due after payment (Jan 16, 00:43)",
                "description": "Detailed pricing breakdown documenting surcharge and outstanding balance demanded after completion of €473.85 payment"
            },
            {
                "type": "image",
                "file": "surcharge proof.PNG",
                "context": "Surcharge proof – Order #16045 (main order)",
                "description": "Documentation of post-payment surcharge imposed on Order #16045"
            },
            {
                "type": "image",
                "file": "surcharge proof smaller order older.PNG",
                "context": "Surcharge proof – smaller/older order",
                "description": "Screenshot of surcharge applied on earlier/smaller order – same post-payment pattern"
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "IV.5 - Illegal Post-Checkout Surcharges",
                "lines": "79-81"
            }
        ]
    },
    
    "§ 5 UWG - Bait Advertising": {
        "law_code": "§ 5 UWG",
        "title": "Drip Pricing & Bait Advertising",
        "description": "The merchant advertises 'Free Shipping' for orders exceeding €99 while concealing mandatory surcharges in minimally visible text within the terms of service. This practice constitutes misleading advertising (drip pricing) and an Unfair Commercial Practice under § 5 of the German Act Against Unfair Competition (UWG), as material information regarding the total cost is withheld from consumers at the point of decision-making.",
        "evidence": [
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-20 at 14.16.30 (1).jpeg",
                "context": "Free shipping advertisement",
                "description": "Documentation of merchant's advertised 'Free Shipping over €99' representation"
            },
            {
                "type": "image",
                "file": "WhatsApp Image 2026-01-16 at 00.43.01 (1).jpeg",
                "context": "Order exceeding €99 with surcharge",
                "description": "€479.70 order charged additional shipping fee"
            },
            {
                "type": "image",
                "file": "surcharge proof.PNG",
                "context": "Surcharge proof – Free Shipping claim vs. surcharge applied",
                "description": "Documentary evidence of surcharge imposition despite order exceeding advertised threshold—supporting misleading advertising claim"
            },
            {
                "type": "image",
                "file": "surcharge proof smaller order older.PNG",
                "context": "Surcharge proof – smaller order (earlier instance)",
                "description": "Earlier order showing same pattern: surcharge despite threshold/claims"
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "IV.6 - Drip Pricing & Bait Advertising",
                "lines": "83-87"
            }
        ]
    },
    
    "EU Directive 2005/29/EC - Aggressive Practice": {
        "law_code": "EU Dir. 2005/29/EC",
        "title": "Aggressive Commercial Practice",
        "description": "Withholding fully paid goods to demand additional payment constitutes an 'Aggressive Commercial Practice' under Article 8 of EU Directive 2005/29/EC on Unfair Commercial Practices. Such conduct significantly impairs consumer freedom of choice through coercion. Additionally, the merchant engaged in a sustained pattern of repeatedly confirming and subsequently cancelling identical orders (including #16142, #16144, #16161, #16245) within short timeframes, accompanied by excessive subscription reminders, abandoned cart notifications, and payment-failure alerts. This systematic barrage of contradictory communications creates undue pressure on the consumer. Furthermore, the merchant continues to retain consumer funds, with refunds designated as 'upcoming' (e.g., expected 6 February), demonstrating a recurring pattern of fund retention that further compounds the aggressive commercial practice.",
        "evidence": [
            {
                "type": "image",
                "file": "inbox_harassment_confirm_cancel.png",
                "context": "Inbox – repeated confirm/cancel (Jan 2026)",
                "description": "Documentation of repeated confirmations and subsequent cancellations of identical orders (#16245, #16161, #16144, #16142), accompanied by excessive subscription and cart notifications—demonstrating systematic pattern of contradictory communications"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_1.png",
                "context": "Revolut transactions – aggressive charging/refunding (Jan 16-26, 2026)",
                "description": "Pattern of aggressive commercial practice: Jan 16 -€473.85, then multiple charges and refunds (Jan 19, Jan 24 -€123.20 x2, +€473.85), upcoming refunds €123.20 x3 — withholding goods by constant charge/refund cycle; creates coercion and confusion"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_2.png",
                "context": "Revolut transactions – Jan 24 charge/refund cycle",
                "description": "Jan 24 transaction sequence: dual charges of -€123.20 ×2 at 11:02, followed by refund of +€473.85 at 03:40—evidence of coercive charge/refund pattern"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_3.png",
                "context": "Revolut transactions – Jan 25–28 refunds after charge (Feb 1, 2026)",
                "description": "Transaction sequence: Jan 25 charge -€123.20; Jan 27 dual refunds +€123.20 ×2; Jan 28 refund +€123.20—demonstrating coercive charge-and-refund pattern"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_4.png",
                "context": "Revolut transactions – Jan 24–25 charges and €473.85 refund",
                "description": "Jan 24 -€123.20 x2 at 11:02, +€473.85 refund at 03:40; Jan 25 -€123.20 at 11:01 — constant charging and refunding"
            },
            {
                "type": "image",
                "file": "revolut_transactions_charge_refund_5.png",
                "context": "Revolut transactions – taking and holding money (Feb 1, 2026)",
                "description": "Evidence of fund retention constituting aggressive practice: refund of +€123.20 designated as 'upcoming' with expected date of 6 February—consumer funds being retained by merchant; recent charge -€123.20 at 11:02; Jan 28 refund +€123.20—demonstrating recurring pattern of fund retention"
            },
            {
                "type": "pdf",
                "file": "2026-01-20-ORDER _16045 REJECTION OF UNILATERAL REFUND _ NOTICE OF REGULATORY ACTION.pdf",
                "context": "Rejection of refund - demand for delivery",
                "description": "Formal legal notice rejecting merchant's unilateral cancellation and demanding specific performance"
            },
            {
                "type": "document",
                "file": "data/eml_extract_refund_rejection_2026_01_20.md",
                "context": "Rejection of Unilateral Refund – full extract",
                "description": "Full extracted text of ORDER #16045 REJECTION OF UNILATERAL REFUND – NOTICE OF REGULATORY ACTION email (20 Jan 2026); §§ 280, 281, 286 BGB; 12h remediation; regulatory filings."
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "IV.7 - Aggressive Commercial Practice",
                "lines": "89-93"
            }
        ]
    },
    
    "§ 433 BGB - Material Breach": {
        "law_code": "§ 433 BGB",
        "title": "Material Breach of Contract",
        "description": "A portion of the delivered goods failed to meet merchantable quality standards, including: spoiled milk products, items contaminated with unidentified black adhesive substances, and approximately five packages with punctured or compromised packaging. While these defective items represent a minority of the total delivery, they nonetheless constitute material breaches of contract under § 433 BGB (obligation to deliver goods of merchantable quality). The consumer reserves the right to pursue remedies for these breaches, conditional upon the merchant's fulfillment of the agreed subscription terms and delivery obligations.",
        "evidence": [
            {
                "type": "image",
                "file": "IMG-20251225-WA0001.jpg",
                "context": "Rotten Milk Evidence (Dec 25, 2025)",
                "description": "Photographic documentation of defective product (spoiled milk)—representative of quality deficiencies affecting minority of delivery"
            },
            {
                "type": "image",
                "file": "IMG-20251225-WA0003.jpg",
                "context": "Contaminated Product (Dec 25, 2025)",
                "description": "One of the affected items – visible contamination (minority of delivery)"
            },
            {
                "type": "image",
                "file": "IMG-20251225-WA0005.jpg",
                "context": "Undrinkable product (Dec 25, 2025)",
                "description": "Photographic documentation of product quality concern—consumer inquiry to merchant 'Is this drinkable?'—representative of deficiencies affecting minority of delivery"
            },
            {
                "type": "image",
                "file": "IMG-20251225-WA0007.jpg",
                "context": "Additional Defective Product (Dec 25, 2025)",
                "description": "One of the affected items – product defects (minority of delivery)"
            },
            {
                "type": "image",
                "file": "IMG-20251219-WA0010.jpg",
                "context": "Damaged/Punctured Packages (Dec 19, 2025)",
                "description": "Photographic documentation of damaged packaging—approximately five packages received with punctures or compromised integrity"
            },
            {
                "type": "chat",
                "file": "WhatsApp Chat with Made in Market.txt",
                "excerpt": "Lines 33-36",
                "context": "Report of rotten milk to seller",
                "quote": "Is this drinkable?"
            },
            {
                "type": "document",
                "file": "2026-01-20-Default_Notice_Email_Content.txt",
                "section": "III - Unresolved Material Breaches",
                "lines": "184"
            }
        ]
    }
}

# Image context mapping - specific labels for each image
IMAGE_CONTEXTS = {
    "IMG-20251211-WA0001.jpg": {
        "context": "Product Replacement Specs - Parmalat (Dec 11, 2025)",
        "description": "Nutritional information for Parmalat replacement product",
        "category": "product_info"
    },
    "IMG-20251211-WA0002.jpg": {
        "context": "Product Replacement Specs - Parmalat Label (Dec 11, 2025)",
        "description": "Product label showing 0.5% fat, lactose-free confirmation",
        "category": "product_info"
    },
    "IMG-20251211-WA0003.jpg": {
        "context": "Product Replacement Specs - Parmalat Details (Dec 11, 2025)",
        "description": "Additional product specifications",
        "category": "product_info"
    },
    "IMG-20251219-WA0010.jpg": {
        "context": "Damaged/Punctured Packages (Dec 19, 2025)",
        "description": "Photographic documentation of damaged packaging—approximately five packages received with punctures or compromised integrity",
        "category": "breach_evidence",
        "violation": "§ 433 BGB - Material Breach"
    },
    "IMG-20251225-WA0001.jpg": {
        "context": "Rotten Milk Evidence (Dec 25, 2025)",
        "description": "Photographic documentation of defective product (spoiled milk)—representative of quality deficiencies affecting minority of delivery",
        "category": "breach_evidence",
        "violation": "§ 433 BGB - Material Breach"
    },
    "IMG-20251225-WA0003.jpg": {
        "context": "Contaminated Product (Dec 25, 2025)",
        "description": "Photographic documentation of contaminated product—representative of quality deficiencies affecting minority of delivery",
        "category": "breach_evidence",
        "violation": "§ 433 BGB - Material Breach"
    },
    "IMG-20251225-WA0005.jpg": {
        "context": "Undrinkable Product Quality (Dec 25, 2025)",
        "description": "Photographic documentation of product quality concern—consumer inquiry to merchant 'Is this drinkable?'—representative of deficiencies affecting minority of delivery",
        "category": "breach_evidence",
        "violation": "§ 433 BGB - Material Breach"
    },
    "IMG-20251225-WA0007.jpg": {
        "context": "Additional Defective Product (Dec 25, 2025)",
        "description": "One of the affected items – product quality issues (minority of delivery)",
        "category": "breach_evidence",
        "violation": "§ 433 BGB - Material Breach"
    },
    "WhatsApp Image 2026-01-16 at 00.40.52.jpeg": {
        "context": "Post-payment surcharge notice (Jan 16, 2026)",
        "description": "Documentation of post-payment surcharge demand: additional €150 surcharge imposed after completion of €473.85 payment",
        "category": "pricing_violation",
        "violation": "§ 312a Abs. 3 BGB - Post-Checkout Surcharges"
    },
    "WhatsApp Image 2026-01-16 at 00.41.58.jpeg": {
        "context": "Payment confirmation – Revolut €473.85 (Jan 16, 2026)",
        "description": "Proof of full payment before surcharge demand",
        "category": "pricing_violation",
        "violation": "§ 312a Abs. 3 BGB - Post-Checkout Surcharges"
    },
    "WhatsApp Image 2026-01-16 at 00.43.01 (1).jpeg": {
        "context": "Order details – surcharge applied (Jan 16, 2026)",
        "description": "Order exceeding €99 with additional shipping fee demanded after payment",
        "category": "pricing_violation",
        "violation": "§ 5 UWG - Bait Advertising"
    },
    "WhatsApp Image 2026-01-16 at 00.43.39.jpeg": {
        "context": "Order breakdown – balance due after payment (Jan 16, 2026)",
        "description": "Pricing breakdown showing surcharge/balance demanded after €473.85 paid",
        "category": "pricing_violation",
        "violation": "§ 312a Abs. 3 BGB - Post-Checkout Surcharges"
    },
    "WhatsApp Image 2026-01-20 at 14.16.30 (1).jpeg": {
        "context": "Terms of Service – hidden surcharge clause (Jan 20, 2026)",
        "description": "Documentation of shipping policy explicitly stating that additional fees are disclosed after order placement",
        "category": "legal_violation",
        "violation": "§ 312j BGB - Button Solution Violation"
    },
    "shipping_policy_pre_full_page.png": {
        "context": "Shipping Policy – PRE: full page (Item 12 buried at bottom) (Jan 20, 2026)",
        "description": "Full-page PRE screenshot: madeinmarket.eu/policies/shipping-policy – Clause 12 (heavy/bulky surcharge, informed after order) in micro-text at bottom",
        "category": "legal_violation",
        "violation": "§ 312j BGB - Button Solution Violation"
    },
    "shipping_policy_item12_back_down_feb2026.png": {
        "context": "Shipping Policy – Item 12 moved back down (Feb 2026)",
        "description": "Approx. two weeks after consumer's last written communication (Binding Confirmation, 22 Jan 2026), merchant moved surcharge clause (Item 12) back to bottom of madeinmarket.eu/policies/shipping-policy—earlier change was temporary; clause again in minimal prominence.",
        "category": "legal_violation",
        "violation": "§ 312j BGB - Button Solution Violation"
    },
    "WhatsApp Image 2026-01-20 at 15.21.08 (1).jpeg": {
        "context": "Shipping Policy - POST: clause moved higher (Jan 20, 2026)",
        "description": "Documentation of revised policy following receipt of consumer's Default Notice—clause repositioned to more prominent location; however, violation persists as total price remains absent from purchase button and post-payment charges remain legally void",
        "category": "legal_violation",
        "violation": "§ 305c BGB - Surprising Clause"
    },
    "WhatsApp Image 2026-01-21 at 19.16.03 (1).jpeg": {
        "context": "Additional Documentation (Jan 21, 2026)",
        "description": "Supporting evidence for legal claims",
        "category": "legal_violation"
    },
    "WhatsApp Image 2026-01-21 at 19.21.13 (1).jpeg": {
        "context": "Further Evidence (Jan 21, 2026)",
        "description": "Additional proof of violations",
        "category": "legal_violation"
    },
    "surcharge proof.PNG": {
        "context": "Surcharge proof – Order #16045 (main order)",
        "description": "Screenshot of post-payment surcharge demanded on main order #16045",
        "category": "pricing_violation",
        "violation": "§ 312a Abs. 3 BGB - Post-Checkout Surcharges"
    },
    "surcharge proof smaller order older.PNG": {
        "context": "Surcharge proof – smaller/older order",
        "description": "Documentation of surcharge applied on earlier order—demonstrating consistent pattern of post-payment surcharge imposition",
        "category": "pricing_violation",
        "violation": "§ 312a Abs. 3 BGB - Post-Checkout Surcharges"
    },
    "inbox_harassment_confirm_cancel.png": {
        "context": "Inbox – repeated confirm/cancel (Jan 2026)",
        "description": "Same orders confirmed then cancelled repeatedly; subscription and cart emails – constant confirming, informing, cancelling",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    },
    "revolut_transactions_charge_refund_1.png": {
        "context": "Revolut transactions – constant charge/refund pattern (Jan 16-26, 2026)",
        "description": "Documentation of multiple charge and refund transactions creating consumer confusion: Jan 16 charge -€473.85, Jan 19 refund +€123.20, Jan 24 dual charges -€123.20 ×2 followed by refund +€473.85, with three pending refunds of €123.20 each",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    },
    "revolut_transactions_charge_refund_2.png": {
        "context": "Revolut transactions – Jan 24 charges and refund",
        "description": "Jan 24 charge/refund cycle: -€123.20 x2 at 11:02, +€473.85 refund at 03:40 – coercive pattern",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    },
    "revolut_transactions_charge_refund_3.png": {
        "context": "Revolut transactions – Jan 25–28 charge/refund cycle (Feb 1, 2026)",
        "description": "Transaction sequence: Jan 25 charge -€123.20; Jan 27 dual refunds +€123.20 ×2; Jan 28 refund +€123.20—demonstrating repeated charge-and-refund pattern",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    },
    "revolut_transactions_charge_refund_4.png": {
        "context": "Revolut transactions – Jan 24–25 charges and refund",
        "description": "Transaction sequence: Jan 24 dual charges -€123.20 ×2, refund +€473.85; Jan 25 charge -€123.20—evidence of systematic charging and refunding",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    },
    "revolut_transactions_charge_refund_5.png": {
        "context": "Revolut transactions – taking and holding money (Feb 1, 2026)",
        "description": "Evidence of fund retention: refund of +€123.20 designated as 'upcoming' with expected date of 6 February—consumer funds being retained by merchant; demonstrates recurring pattern of fund retention",
        "category": "legal_violation",
        "violation": "EU Directive 2005/29/EC - Aggressive Practice"
    }
}

def get_evidence_for_violation(violation_key):
    """Get all evidence items for a specific violation"""
    return EVIDENCE_MAP.get(violation_key, {}).get("evidence", [])

def get_violations_for_image(image_filename):
    """Get all violations related to a specific image"""
    violations = []
    for violation_key, violation_data in EVIDENCE_MAP.items():
        for evidence in violation_data.get("evidence", []):
            if evidence.get("type") == "image" and evidence.get("file") == image_filename:
                violations.append(violation_key)
    return violations

def get_image_context(image_filename):
    """Get detailed context for an image"""
    return IMAGE_CONTEXTS.get(image_filename, {
        "context": image_filename,
        "description": "Evidence file",
        "category": "general"
    })
