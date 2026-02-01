# Timeline data – quick navigation

All timeline event files are **under 500 lines** for easy editing and navigation.

## File map (by date)

| File | Period | ~Lines | Contents |
|------|--------|--------|----------|
| `timeline_events_2025.py` | Nov–Dec 2025 | ~230 | Orders #15073, #15179, #15341; supplier/UCAL; WhatsApp Dec 11–29; damage evidence |
| `timeline_events_2025_emails.py` | Nov–Dec 2025 | ~220 | Email notifications + support thread content (discount bug, skip requests, dispatch, Parmalat conditions) |
| `timeline_events_2026_jan_10_19.py` | Jan 10–19, 2026 | ~400 | Order #15977/#16045; surcharges; legal notices; deadline Jan 19 |
| `timeline_events_2026_jan_20_default.py` | Jan 20 (default) | ~200 | Default Notice (Verzug); sections I–VII; violations/demands |
| `timeline_events_2026_jan_20_policy.py` | Jan 20 (policy) | ~390 | ToS/Shipping Policy evidence: thresholds, fees, payment terms, returns, customs, disclaimers |
| `timeline_events_2026_jan_20_policy_site.py` | Jan 20 (site terms) | ~120 | Website terms: access, conduct, IP, legal entity, jurisdiction |
| `timeline_events_2026_jan_20_policy_dispute.py` | Jan 20 (dispute details) | ~70 | ADR list, complaint email, venue clauses |
| `timeline_events_2026_jan_20_policy_environment.py` | Jan 20 (environment) | ~40 | Environmental packaging/recycling commitments |
| `timeline_events_2026_jan_20_rejection.py` | Jan 20–21 (rejection) | ~420 | Rejection of unilateral refund; procedures; evidence list |
| `timeline_events_2026_jan_22_articles_i_v.py` | Jan 22 | ~320 | Binding confirmation: definitions, subscription, term, force majeure |
| `timeline_events_2026_jan_22_articles_vi_viii.py` | Jan 22 | ~200 | Remedies, settlement/abeyance, general provisions |
| `timeline_events_2026_jan_24_26.py` | Jan 24–26 | ~60 | Orders #16142/#16144/#16161; call log |
| `timeline_events_2026_jan_31.py` | Jan 31 | ~20 | Order #16245 confirmation |
| `timeline_events_2026_jan_email_notifications.py` | Jan 10–28 | ~200 | Verification codes, cart promos, payment failure, updates/cancellations |
| `timeline_events_email_links.py` | Nov 2025–Jan 2026 | ~140 | Secure order-view links in confirmations/shipping emails (sanitized) |
| `timeline_events_email_payment_links.py` | Nov 2025–Jan 2026 | ~40 | Payment link issuance from order update emails |
| `timeline_events_email_confirmation_details.py` | Nov 2025–Jan 2026 | ~80 | Weekly delivery cadence noted in confirmations |
| `timeline_events_email_fulfillment_promises.py` | Nov 2025–Jan 2026 | ~120 | “Order ready to ship” + notify when sent |
| `timeline_events_email_tracking_prompts.py` | Dec 2025 | ~40 | Shipping emails prompting tracking |
| `timeline_events_email_verification_terms.py` | Jan 2026 | ~30 | Verification code one-time use + 15‑minute expiry |
| `timeline_events_email_verification_codes.py` | Jan 2026 | ~20 | Verification email code values |
| `timeline_events_email_fee_breakdowns.py` | Jan 2026 | ~80 | Cancellation email fee/tax breakdowns |
| `timeline_events_email_cancellation_markers.py` | Jan 2026 | ~60 | Cancellation labels: weekly delivery + discount flags |
| `timeline_events_email_refund_labels.py` | Jan 2026 | ~60 | “Refunded Items” section labels |
| `timeline_events_email_payment_methods.py` | Jan 2026 | ~30 | Payment method mentions in cancellations |
| `timeline_events_email_pricing_mentions.py` | Nov 2025 | ~20 | Support pricing clarifications (per‑unit pricing) |
| `timeline_events_email_update_reasons.py` | Nov 2025–Jan 2026 | ~40 | Order update reasons (out‑of‑stock, substitutions, fee adjustments) |
| `timeline_events_email_update_shipping_surcharge.py` | Jan 2026 | ~20 | Order update surcharge line item (heavy/voluminous shipping) |
| `timeline_events_email_update_cta.py` | Nov 2025–Jan 2026 | ~40 | Update emails request review/response |
| `timeline_events_email_update_sections.py` | Nov 2025–Jan 2026 | ~40 | Update email summary sections (updated total, already paid, amount to pay, etc.) |
| `timeline_events_email_update_action_required.py` | Nov 2025–Jan 2026 | ~30 | Update emails warning of required action and delays until resolved |
| `timeline_events_email_update_review_request.py` | Nov 2025–Jan 2026 | ~30 | Update emails asking customer to review changes and contact if they disagree |
| `timeline_events_email_update_review_links.py` | Nov 2025–Jan 2026 | ~30 | Update emails including Trustpilot review links |
| `timeline_events_email_contact_channels.py` | Nov 2025–Jan 2026 | ~60 | WhatsApp/support email contact channels |
| `timeline_events_email_policy_links.py` | Jan 2026 | ~30 | Verification emails with Privacy/Terms links |
| `timeline_events_email_support_attachment_mentions.py` | Nov–Dec 2025 | ~40 | Support emails referencing screenshots/photos |
| `timeline_events_email_support_followups.py` | Dec 2025 | ~40 | Support notes: subscription canceled, company purchase inquiry |
| `timeline_events_email_support_tracking_number.py` | Dec 2025 | ~20 | Support dispatch email with tracking number (Dachser) |
| `timeline_events_email_support_carrier.py` | Dec 2025 | ~20 | Support dispatch email with carrier/mode (Dachser pallet transport) |
| `timeline_events_email_support_nutrition_specs.py` | Dec 2025 | ~30 | Support nutrition specs (fat and lactose levels, lactose-free label) |
| `timeline_events_email_support_subscription_continuation.py` | Dec 2025 | ~20 | Support note about continuing subscription unless told otherwise |
| `timeline_events_email_delay_explanations.py` | Dec 2025 | ~40 | Delay reasons (holiday/high volume) |
| `timeline_events_email_apologies.py` | Dec 2025 | ~30 | Support apology language |
| `timeline_events_email_product_change.py` | Dec 2025 | ~40 | UCAL → Parmalat explanation + specs confirmation |
| `timeline_events_email_support_diagnostics.py` | Nov 2025 | ~40 | Support diagnostics: bug fix + recurring order simulation |
| `timeline_events_email_marketing_details.py` | Nov 2025–Jan 2026 | ~90 | Marketing emails: abandoned carts, discounts, countdown |
| `timeline_events_email_marketing_stock_warning.py` | Nov 2025–Jan 2026 | ~30 | Reserved stock warning in abandoned-cart emails |
| `timeline_events_email_marketing_discount_codes.py` | Nov 2025–Jan 2026 | ~40 | Marketing discount codes (MadeinMarket20/MadeinMarket5) |
| `timeline_events_email_marketing_discount_cta.py` | Nov 2025–Jan 2026 | ~40 | Marketing discount CTA instructions (use code or click link) |
| `timeline_events_email_marketing_checkout_cta.py` | Nov 2025–Jan 2026 | ~30 | Abandoned cart “Continue checkout” CTA button |
| `timeline_events_email_marketing_unsubscribe_links.py` | Nov 2025–Jan 2026 | ~60 | Marketing emails with unsubscribe link info |
| `timeline_events_email_marketing_reservation_notice.py` | Nov 2025–Jan 2026 | ~30 | Abandoned cart “products reserved” notices |
| `timeline_events_email_marketing_first_time_customer.py` | Nov 2025 | ~20 | First-time customer 20% discount mention |
| `timeline_events_email_marketing_signoff.py` | Nov 2025–Jan 2026 | ~30 | Marketing sign-off thanks and “look forward to your order” |
| `timeline_events_email_marketing_cart_quantities.py` | Nov 2025–Jan 2026 | ~40 | Abandoned cart quantities and reserved-stock note |
| `timeline_events_email_marketing_delivery_cutoffs.py` | Nov–Dec 2025 | ~30 | Holiday delivery cutoff details (Christmas/Eve, standard vs express) |
| `timeline_events_email_subscription_terms.py` | Nov 2025–Jan 2026 | ~30 | Subscription confirmation terms about ongoing weekly billing |
| `timeline_events_email_payment_failure_cta.py` | Jan 2026 | ~20 | Payment failure email CTA to update payment method |
| `timeline_events_email_payment_failure_body.py` | Jan 2026 | ~20 | Payment failure email body text (couldn’t be processed; update method) |
| `timeline_events_email_payment_failure_sections.py` | Jan 2026 | ~20 | Payment failure email sections (order summary, payment, shipping method) |
| `timeline_events_email_payment_failure_manage_link.py` | Jan 2026 | ~20 | Payment failure manage-subscription link |
| `timeline_events_email_payment_failure_update_link.py` | Jan 2026 | ~20 | Payment failure update-payment-method link |
| `timeline_events_email_payment_failure_cadence.py` | Jan 2026 | ~20 | Payment failure email mentions weekly delivery cadence |
| `timeline_events_email_purchase_thanks.py` | Nov 2025–Jan 2026 | ~90 | Order confirmation “thank you” acknowledgements |
| `timeline_events_email_shipping_status.py` | Dec 2025 | ~40 | Shipping emails stating orders are on the way |
| `timeline_events_email_shipping_view_order_cta.py` | Dec 2025 | ~30 | Shipping emails with “View your order” CTA |
| `timeline_events_email_cancellation_language.py` | Jan 2026 | ~60 | Cancellation emails with standard “order has been canceled” language |
| `timeline_events_email_cancellation_sections.py` | Jan 2026 | ~40 | Cancellation email summary sections (refunded items, subtotal, taxes, total) |
| `timeline_events_email_cancellation_contact.py` | Jan 2026 | ~40 | Cancellation emails with contact instructions |
| `timeline_events_email_subscription_manage_links.py` | Nov 2025–Jan 2026 | ~90 | Manage‑subscription links in reminder/cancellation emails |
| `timeline_events_email_review_links.py` | Nov–Dec 2025 | ~30 | Trustpilot review links in dispatch/shipping emails |
| `timeline_events_email_payment_due_amounts.py` | Nov 2025–Jan 2026 | ~40 | Order update emails stating payment due amounts |
| `timeline_events_email_subscription_acknowledgements.py` | Nov 2025–Jan 2026 | ~30 | Subscription confirmation thank‑you acknowledgements |
| `timeline_events_email_subscription_shipping_notice.py` | Nov 2025–Jan 2026 | ~30 | Subscription confirmations stating customer will be notified when sent |
| `timeline_events_email_subscription_charge_notice.py` | Nov 2025–Jan 2026 | ~50 | Subscription reminders stating upcoming order will be charged soon |
| `timeline_events_email_subscription_change_deadlines.py` | Nov 2025–Jan 2026 | ~50 | Reminder emails with specific change-by deadlines |
| `timeline_events_email_subscription_amounts.py` | Nov 2025–Jan 2026 | ~50 | Reminder emails with upcoming charge amounts |
| `timeline_events_email_subscription_quantities.py` | Nov 2025–Jan 2026 | ~50 | Reminder emails with quantity (×70) in order summary |
| `timeline_events_email_subscription_shipping_method.py` | Nov 2025–Jan 2026 | ~50 | Reminder emails listing FREE Shipping - UPS Standard® |
| `timeline_events_email_subscription_confirmation_shipping_method.py` | Nov 2025–Jan 2026 | ~30 | Subscription confirmations listing FREE Shipping - UPS Standard® |
| `timeline_events_email_subscription_confirmation_manage_links.py` | Nov 2025–Jan 2026 | ~20 | Subscription confirmations with manage-subscription link |
| `timeline_events_email_subscription_confirmation_sections.py` | Nov 2025–Jan 2026 | ~20 | Subscription confirmation sections (order summary, shipping method) |
| `timeline_events_email_subscription_confirmation_totals.py` | Nov 2025–Jan 2026 | ~20 | Subscription confirmation totals (€109.20 / €123.20) |
| `timeline_events_email_subscription_confirmation_discount_marker.py` | Dec 2025 | ~20 | Quoted subscription confirmation “deliver every week, 20% off” marker |
| `timeline_events_email_subscription_confirmation_customer_info.py` | Dec 2025 | ~20 | Quoted subscription confirmation customer information section |
| `timeline_events_email_subscription_confirmation_map_link.py` | Dec 2025 | ~20 | Quoted subscription confirmation map link for shipping address |
| `timeline_events_email_subscription_confirmation_subtotals.py` | Dec 2025 | ~20 | Quoted subscription confirmation subtotal/shipping/taxes (€109.20/€0.00/€7.14) |
| `timeline_events_email_subscription_cadence.py` | Nov 2025–Jan 2026 | ~50 | Reminder emails noting weekly delivery cadence |
| `timeline_events_email_order_ready.py` | Nov 2025–Jan 2026 | ~90 | Confirmation emails stating orders are being prepared for shipment |
| `timeline_events_email_order_view_cta.py` | Nov 2025–Jan 2026 | ~90 | Confirmation emails with “View your order” CTA |
| `timeline_events_email_subscription_change_window.py` | Nov 2025–Jan 2026 | ~50 | Subscription reminder change‑before window notices |
| `timeline_events_email_greetings.py` | Nov 2025 | ~20 | Formal greeting in dispatch email |
| `timeline_events_email_signoffs.py` | Nov 2025 | ~20 | Formal sign-off in dispatch email |
| `timeline_events_email_refund_amounts.py` | Jan 2026 | ~40 | Cancellation emails stating refund amounts |
| `timeline_events_email_shipment_quantities.py` | Dec 2025 | ~20 | Support dispatch email with shipment quantity (178 units) |
| `timeline_events_email_cancellation_quantities.py` | Jan 2026 | ~60 | Cancellation emails listing product quantities |
| `timeline_events_email_dispatch_plan.py` | Nov 2025 | ~20 | Dispatch plan note for Orders #15073/#15179 |
| `timeline_events_email_product_mentions_confirmations.py` | Nov 2025–Jan 2026 | ~90 | Product names referenced in order confirmations |
| `timeline_events_email_product_mentions_reminders.py` | Nov 2025–Jan 2026 | ~50 | Product names referenced in subscription reminders |
| `timeline_events_email_order_summary_sections.py` | Nov 2025–Jan 2026 | ~50 | Subscription reminder “order summary” sections |
| `timeline_events_email_cancellation_refund_method.py` | Jan 2026 | ~20 | Cancellation emails noting refund method |
| `timeline_events_email_cancellation_effects.py` | Dec 2025 | ~20 | Cancellation email stating no upcoming orders |
| `timeline_events_email_cancellation_subjects.py` | Jan 2026 | ~40 | Cancellation email subject lines |
| `timeline_events_email_marketing_subjects.py` | Nov 2025–Jan 2026 | ~60 | Marketing email subject lines |
| `timeline_events_email_confirmation_subjects.py` | Nov 2025–Jan 2026 | ~90 | Order confirmation email subject lines |
| `timeline_events_email_confirmation_shipping_method.py` | Nov 2025–Jan 2026 | ~90 | Confirmation emails listing FREE Shipping - UPS Standard® |
| `timeline_events_email_confirmation_sections.py` | Nov 2025–Jan 2026 | ~90 | Confirmation email summary sections (order summary/shipping) |
| `timeline_events_email_confirmation_store_cta.py` | Dec 2025 | ~20 | Quoted confirmation “Visit our store” CTA |
| `timeline_events_email_shipping_subjects.py` | Dec 2025 | ~30 | Shipping email subject lines |
| `timeline_events_email_shipping_labels.py` | Dec 2025 | ~30 | Shipping email labels (other tracking, items in shipment, refunded) |
| `timeline_events_email_system_subjects.py` | Nov 2025–Jan 2026 | ~80 | System email subject lines (verification, payment failure, reminders) |
| `timeline_events_email_binding_confirmation_body.py` | Jan 2026 | ~20 | Binding confirmation email: acceptance by reply or performance |
| `timeline_events_email_support_subjects.py` | Nov–Dec 2025 | ~40 | Support thread subject lines |
| `timeline_events_email_customer_subjects.py` | Nov–Dec 2025 | ~60 | Customer email subject lines |
| `timeline_events_email_customer_confirmation_requests.py` | Dec 2025 | ~40 | Customer requests to confirm receipt of skip requests |
| `timeline_events_email_customer_skip_rationale.py` | Dec 2025 | ~30 | Customer skip requests citing double amount shipped |
| `timeline_events_email_customer_shipment_quantity_claim.py` | Dec 2025 | ~20 | Customer claim of 140 units covering two weeks |
| `timeline_events_email_customer_weekly_requirement.py` | Dec 2025 | ~20 | Customer statement of 70 units/week requirement |
| `timeline_events_email_legal_subjects.py` | Jan 2026 | ~30 | Legal email subject lines (default, rejection, binding confirmation) |
| `timeline_events_email_update_subjects.py` | Nov 2025–Jan 2026 | ~30 | Order update email subject lines |
| `timeline_events_email_subscription_cancellation_contact.py` | Dec 2025 | ~20 | Subscription cancellation contact instructions |
| `timeline_events_email_subscription_cancellation_subjects.py` | Dec 2025 | ~20 | Subscription cancellation subject line |
| `timeline_events_email_support_requests.py` | Nov 2025 | ~20 | Support requests for screenshots and shipping details |
| `timeline_events_email_dispatch_cta.py` | Nov 2025 | ~20 | Dispatch email CTA inviting changes/questions |
| `timeline_events_email_subscription_subjects.py` | Nov 2025–Jan 2026 | ~20 | Subscription confirmation email subject lines |
| `timeline_events_email_update_delay_warnings.py` | Nov 2025–Jan 2026 | ~40 | Update emails warning of delays until balance/action resolved |
| `timeline_events_email_payment_failure_delay_warning.py` | Jan 2026 | ~20 | Payment failure delay warning |
| `timeline_events_email_support_vat_request.py` | Dec 2025 | ~20 | Support request for DE VAT ID |
| `timeline_events_email_support_trustpilot_note.py` | Nov 2025 | ~20 | Support note about Trustpilot email after shipment |
| `timeline_events_email_support_bbd_note.py` | Dec 2025 | ~20 | Support note about Parmalat batch/BBD 14/03/26 |
| `timeline_events_email_support_pricing_market_mismatch.py` | Dec 2025 | ~20 | Support note: screenshot shows Portuguese market pricing |
| `timeline_events_email_support_producer_reassurance.py` | Dec 2025 | ~20 | Support reassurance: producer double-checked nutrition |
| `timeline_events_email_support_error_message.py` | Nov 2025 | ~20 | Support reference to “Shipping not available” error |
| `timeline_events_email_support_discount_display.py` | Dec 2025 | ~20 | Support guidance: discount should display after market fix |
| `timeline_events_email_support_instructions.py` | Nov 2025 | ~20 | Support instructions (retry 58L order, ensure Germany pricing) |

## Aggregators (do not edit event text)

- `timeline_events_2026.py` – imports all 2026 modules
- `timeline_events_2026_jan_20_21.py` – imports default + rejection
- `timeline_events_2026_jan_22.py` – imports articles I–V + VI–VIII
- `timeline_events_2026_jan_early.py` – Jan 10–19 + Jan 20–21
- `timeline_events_2026_jan_late.py` – Jan 22 + Jan 24–26
- `timeline_events.py` – imports 2025 + 2026 + email detail modules; used by app

## Evidence

- `evidence_mapping.py` – file names → display names, dates, context
- `evidence_loader.py` – loads evidence files for views
