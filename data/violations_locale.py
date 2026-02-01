# Violations page locale / jurisdiction switch
# Change DEFAULT_JURISDICTION or add options here for easy UI switch in code

from data.evidence_mapping import EVIDENCE_MAP

# Jurisdiction options: "de_eu" = English for German/EU laws, "de" = German language, "pt" = Portugal
JURISDICTION_OPTIONS = ["de_eu", "de", "pt"]
DEFAULT_JURISDICTION = "de_eu"

# Same keys as EVIDENCE_MAP (order preserved for display)
VIOLATION_KEYS_ORDER = [k for k in EVIDENCE_MAP.keys() if not k.startswith(("IMG-", "WhatsApp", "surcharge", "shipping_", "inbox_"))]

# Portuguese law codes, titles, descriptions (same keys as EVIDENCE_MAP)
# Citations for ASAE: DL 24/2008, DL 57/2008, DL 446/85, DL 84/2021, Código Civil
TEXTS_PT = {
    "§ 242 BGB - Bad Faith Inducement": {
        "law_code": "Código Civil, Art. 334 (Abuso de Direito) e Art. 227 (Boa-fé pré-contratual)",
        "title": "Violação da boa-fé (Venire contra factum proprium)",
        "description": "O comerciante contactou o consumidor via telefone e insistiu que encomendas em volume eram obrigatórias para beneficiar de portes grátis, afirmando explicitamente que encomendas semanais de 70L não receberiam este benefício. Confiando nesta representação, o consumidor efetuou uma encomenda em volume de 243L. Subsequentemente, o comerciante exigiu um suplemento adicional de €150 e reteve o envio até ao pagamento. Esta conduta contraditória—encorajando compras em volume enquanto simultaneamente impõe suplementos sobre tais compras—constitui violação do princípio da boa-fé (venire contra factum proprium), previsto nos Art. 334 (abuso de direito) e Art. 227 (responsabilidade pré-contratual) do Código Civil. Adicionalmente, o comerciante envolveu-se num padrão de confirmações e cancelamentos repetidos dos mesmos números de encomenda (ex.: #16142, #16144, #16161, #16245), gerando comunicações excessivas e contraditórias. O comerciante continua a reter fundos do consumidor, com reembolsos designados como 'previstos' (ex.: 6 de fevereiro), demonstrando um padrão recorrente de retenção de fundos."
    },
    "§ 312j BGB - Button Solution Violation": {
        "law_code": "DL 24/2008, Art. 5.º n.º 1 alínea g) e Art. 8.º n.º 2 — Dever de informação pré-contratual",
        "title": "Violação do preço total no botão de compra (dever de informação pré-contratual)",
        "description": "O Art. 5.º n.º 1 alínea g) do DL 24/2008 exige que o preço total, incluindo todos os impostos e encargos de transporte/entrega, seja claramente indicado antes da conclusão do contrato. O Art. 8.º n.º 2 estabelece que, se o botão de finalização da encomenda não apresentar claramente o preço total, o consumidor não fica vinculado ao contrato. A política de envios do comerciante declara explicitamente que taxas adicionais são informadas após a colocação da encomenda, constituindo violação direta do dever de informação pré-contratual. Inicialmente, a cláusula de suplemento encontrava-se posicionada no ponto 12, no final da política, em fonte de tamanho mínimo. Após receção do Aviso de Incumprimento formal do consumidor (declaração de Verzug com exigência de cumprimento específico), o comerciante reposicionou a cláusula para uma posição mais proeminente. Contudo, esta revisão não remedeia a violação: o preço total permanece ausente do botão de compra, e a política continua a afirmar que encargos adicionais são 'informados após colocar a encomenda.' Cobranças pós-pagamento permanecem juridicamente nulas independentemente da localização da cláusula na política."
    },
    "§ 305c BGB - Surprising Clause": {
        "law_code": "DL 446/85, Art. 18.º e 19.º (Lei das Cláusulas Contratuais Gerais)",
        "title": "Cláusulas abusivas / surpresa (DL 446/85)",
        "description": "O DL 446/85 (Lei das Cláusulas Contratuais Gerais) proíbe, nos Art. 18.º e 19.º, cláusulas contratuais inesperadas ou inseridas de forma que o consumidor não pudesse razoavelmente ter conhecimento delas no momento da celebração do contrato. A cláusula de suplemento encontrava-se inicialmente posicionada em fonte de tamanho mínimo no final da política (ponto 12), tornando-a efetivamente oculta à revisão razoável do consumidor. Após receção do Aviso de Incumprimento formal do consumidor (declaração de Verzug com exigência de cumprimento específico), o comerciante reposicionou a cláusula para uma posição mais visível. Contudo, a política revista continua a contradizer a representação 'Portes grátis >€99' exibida no checkout, e as cobranças pós-pagamento permanecem juridicamente nulas. A cláusula de suplemento não era razoavelmente previsível para os consumidores no momento da formação do contrato, constituindo violação dos Art. 18.º e 19.º do DL 446/85."
    },
    "§ 312a Abs. 3 BGB - Post-Checkout Surcharges": {
        "law_code": "DL 24/2008 — cobrança após conclusão do contrato",
        "title": "Suplementos ilegais após conclusão da compra",
        "description": "O comerciante exigiu um suplemento adicional superior a €150 após o consumidor ter já efetuado o pagamento de €473,85. Tais suplementos pós-pagamento requerem consentimento expresso prévio ao abrigo do DL 24/2008. Tal consentimento não foi obtido. Esta exigência de suplemento é juridicamente nula ao abrigo da lei portuguesa e europeia de proteção do consumidor. A prova documental inclui confirmações de encomenda e registos de pagamento que demonstram que o suplemento foi imposto após a conclusão do pagamento."
    },
    "§ 5 UWG - Bait Advertising": {
        "law_code": "DL 57/2008, Art. 7.º (Omissões enganosas)",
        "title": "Publicidade enganosa e «bait advertising»",
        "description": "O comerciante anuncia 'Portes grátis' para encomendas superiores a €99 enquanto oculta suplementos obrigatórios em texto minimamente visível nos termos de serviço. Esta prática constitui publicidade enganosa (drip pricing) e Prática Comercial Desleal ao abrigo do Art. 7.º do DL 57/2008 (transposição da Diretiva 2005/29/CE), uma vez que informação material relativa ao custo total é ocultada dos consumidores no momento da tomada de decisão."
    },
    "EU Directive 2005/29/EC - Aggressive Practice": {
        "law_code": "DL 57/2008, Art. 11.º e 12.º (Prática comercial agressiva)",
        "title": "Prática comercial agressiva (coação)",
        "description": "Reter bens totalmente pagos para exigir pagamento adicional constitui Prática Comercial Agressiva ao abrigo do Art. 11.º e 12.º do DL 57/2008 (transposição do Artigo 8 da Diretiva 2005/29/CE sobre Práticas Comerciais Desleais). Tal conduta prejudica significativamente a liberdade de escolha do consumidor através de coação. Adicionalmente, o comerciante envolveu-se num padrão sistemático de confirmações e cancelamentos repetidos de encomendas idênticas (incluindo #16142, #16144, #16161, #16245) em curtos períodos de tempo, acompanhado por lembretes excessivos de subscrição, notificações de carrinho abandonado e alertas de falha de pagamento. Esta barragem sistemática de comunicações contraditórias cria pressão indevida sobre o consumidor. Além disso, o comerciante continua a reter fundos do consumidor, com reembolsos designados como 'previstos' (ex.: 6 de fevereiro), demonstrando um padrão recorrente de retenção de fundos que agrava a prática comercial agressiva."
    },
    "§ 433 BGB - Material Breach": {
        "law_code": "DL 84/2021, Art. 15.º e 18.º (Regime Jurídico da Venda de Bens de Consumo)",
        "title": "Falta de conformidade dos bens (DL 84/2021)",
        "description": "Uma porção dos bens entregues não satisfez os padrões de qualidade comercializável, incluindo: produtos lácteos deteriorados, artigos contaminados com substâncias adesivas negras não identificadas, e aproximadamente cinco embalagens com perfurações ou integridade comprometida. Embora estes artigos defeituosos representem uma minoria da entrega total, constituem não obstante faltas de conformidade ao abrigo do DL 84/2021 (Art. 15.º - bens conformes, e Art. 18.º - direitos do consumidor à reparação, substituição ou reembolso). O vendedor falhou na entrega de bens com a qualidade comercializável exigida. O consumidor reserva o direito de prosseguir com os remédios legais aplicáveis a estas faltas de conformidade, condicionalmente ao cumprimento pelo comerciante dos termos de subscrição acordados e obrigações de entrega."
    },
}

# German translations (formal legal language)
TEXTS_DE = {
    "§ 242 BGB - Bad Faith Inducement": {
        "law_code": "§ 242 BGB",
        "title": "Verstoß gegen Treu und Glauben (Venire contra factum proprium)",
        "description": """Der Händler kontaktierte den Verbraucher telefonisch und bestand darauf, dass Großbestellungen erforderlich seien, um kostenlosen Versand zu erhalten, wobei er ausdrücklich erklärte, dass wöchentliche 70L-Bestellungen keinen kostenlosen Versand erhalten würden. Im Vertrauen auf diese Zusicherung tätigte der Verbraucher eine Großbestellung über 243L. Anschließend forderte der Händler einen zusätzlichen Aufschlag von €150 und hielt die Lieferung bis zur Zahlung zurück. Dieses widersprüchliche Verhalten—die Förderung von Großbestellungen bei gleichzeitiger Erhebung von Aufschlägen auf solche Bestellungen—stellt einen Verstoß gegen den Grundsatz von Treu und Glauben (§ 242 BGB) dar. Zusätzlich hat sich der Händler in einem Muster wiederholter Bestätigungen und anschließender Stornierungen derselben Bestellnummern (z.B. #16142, #16144, #16161, #16245) engagiert, was zu übermäßigen und widersprüchlichen Mitteilungen führte. Der Händler behält weiterhin Verbrauchermittel ein, wobei Rückerstattungen als „bevorstehend" bezeichnet werden (z.B. erwartet am 6. Februar), was ein wiederkehrendes Muster der Mitteleinbehaltung demonstriert."""
    },
    "§ 312j BGB - Button Solution Violation": {
        "law_code": "§ 312j BGB",
        "title": "Verstoß gegen die Button-Lösung (Preisangabepflicht)",
        "description": """§ 312j BGB schreibt vor, dass der Gesamtpreis einschließlich aller Versand- und Lieferkosten vor der Zahlungsautorisierung deutlich auf dem finalen Bestellbutton angezeigt werden muss. Die Versandrichtlinie des Händlers erklärt ausdrücklich, dass zusätzliche Gebühren nach der Bestellaufgabe offengelegt werden, was einen direkten Verstoß gegen diese Anforderung darstellt. Zunächst war die Aufschlagsklausel in Punkt 12 am Ende der Richtlinie in minimaler Schriftgröße positioniert. Nach Erhalt der formellen Verzugserklärung des Verbrauchers (Verzugserklärung mit Forderung auf Erfüllung) verlegte der Händler die Klausel an eine prominentere Position in der Richtlinie. Etwa zwei Wochen nach der letzten schriftlichen Mitteilung des Verbrauchers (Verbindliche Bestätigung, 22. Januar 2026) verschob der Händler Punkt 12 wieder an das Ende der Versandrichtlinie bei madeinmarket.eu/policies/shipping-policy—die frühere Änderung war vorübergehend und die Praxis der Platzierung der Klausel in minimaler Prominenz wurde wieder aufgenommen. Diese Überarbeitung (und ihre Rückgängigmachung) behebt den Verstoß nicht: Der Gesamtpreis fehlt weiterhin auf dem Bestellbutton, und die Richtlinie erklärt weiterhin, dass zusätzliche Kosten „nach Bestellaufgabe mitgeteilt" werden. Nachzahlungspflichtige Aufschläge bleiben unabhängig von der Platzierung der Klausel rechtlich nichtig."""
    },
    "§ 305c BGB - Surprising Clause": {
        "law_code": "§ 305c BGB",
        "title": "Überraschende Klausel (§ 305c BGB)",
        "description": """Die Aufschlagsklausel war zunächst in minimaler Schriftgröße am Ende der Richtlinie (Punkt 12) positioniert, wodurch sie der angemessenen Überprüfung durch den Verbraucher effektiv entzogen wurde. Nach Erhalt der formellen Verzugserklärung des Verbrauchers (Verzugserklärung mit Forderung auf Erfüllung) verlegte der Händler die Klausel an eine sichtbarere Position. Etwa zwei Wochen nach der letzten schriftlichen Mitteilung des Verbrauchers (Verbindliche Bestätigung, 22. Januar 2026) verschob der Händler Punkt 12 wieder an das Ende der Versandrichtlinie—die frühere Änderung war vorübergehend und die Praxis der Platzierung der Klausel in minimaler Prominenz wurde wieder aufgenommen. Die überarbeitete Richtlinie (und ihre Rückgängigmachung) widerspricht weiterhin der beim Checkout angezeigten Darstellung „Kostenloser Versand >€99", und nachzahlungspflichtige Aufschläge bleiben rechtlich nichtig. Die ergänzende Klausel war für Verbraucher zum Zeitpunkt der Vertragsbildung nicht angemessen vorhersehbar und stellt einen Verstoß gegen § 305c BGB dar. Gemäß § 305c BGB werden Bestimmungen in Allgemeinen Geschäftsbedingungen nicht Vertragsbestandteil, wenn sie so ungewöhnlich sind, dass der Vertragspartner des Verwenders mit ihnen nicht zu rechnen braucht."""
    },
    "§ 312a Abs. 3 BGB - Post-Checkout Surcharges": {
        "law_code": "§ 312a Abs. 3 BGB",
        "title": "Unzulässige Nachzahlungspflichten",
        "description": """Der Händler forderte einen zusätzlichen Aufschlag von über €150, nachdem der Verbraucher bereits eine Zahlung von €473,85 geleistet hatte. Solche Nachzahlungen erfordern gemäß § 312a Abs. 3 BGB eine ausdrückliche vorherige Zustimmung. Eine solche Zustimmung wurde nicht eingeholt. Diese Aufschlagsforderung ist nach deutschem und portugiesischem Verbraucherschutzrecht rechtlich nichtig. § 312a Abs. 3 BGB bestimmt: „Eine Vereinbarung, die auf eine über das vereinbarte Entgelt für die Hauptleistung hinausgehende Zahlung des Verbrauchers gerichtet ist, kann ein Unternehmer mit einem Verbraucher nur ausdrücklich treffen." Die dokumentarischen Beweise umfassen Bestellbestätigungen und Zahlungsnachweise, die belegen, dass der Aufschlag nach Abschluss der Zahlung erhoben wurde."""
    },
    "§ 5 UWG - Bait Advertising": {
        "law_code": "§ 5 UWG",
        "title": "Irreführende Werbung und Drip Pricing (§ 5 UWG)",
        "description": """Der Händler bewirbt „Kostenloser Versand" für Bestellungen über €99, während er obligatorische Aufschläge in minimal sichtbarem Text in den Geschäftsbedingungen verbirgt. Diese Praxis stellt irreführende Werbung (Drip Pricing) und eine unlautere Geschäftspraxis gemäß § 5 des Gesetzes gegen den unlauteren Wettbewerb (UWG) dar, da wesentliche Informationen über die Gesamtkosten den Verbrauchern zum Zeitpunkt der Entscheidungsfindung vorenthalten werden. § 5 UWG verbietet irreführende geschäftliche Handlungen, insbesondere solche, die dem Verbraucher wesentliche Informationen vorenthalten oder auf unklare, unverständliche oder mehrdeutige Weise bereitstellen, wenn dies geeignet ist, den Verbraucher zu einer geschäftlichen Entscheidung zu veranlassen, die er andernfalls nicht getroffen hätte."""
    },
    "EU Directive 2005/29/EC - Aggressive Practice": {
        "law_code": "EU-Richtlinie 2005/29/EG",
        "title": "Aggressive Geschäftspraktik (Art. 8 der Richtlinie 2005/29/EG)",
        "description": """Das Zurückhalten vollständig bezahlter Waren zur Forderung zusätzlicher Zahlung stellt eine „aggressive Geschäftspraxis" gemäß Artikel 8 der EU-Richtlinie 2005/29/EG über unlautere Geschäftspraktiken dar. Ein solches Verhalten beeinträchtigt erheblich die Wahlfreiheit des Verbrauchers durch Nötigung. Zusätzlich hat sich der Händler in einem anhaltenden Muster wiederholter Bestätigungen und anschließender Stornierungen identischer Bestellungen (einschließlich #16142, #16144, #16161, #16245) innerhalb kurzer Zeiträume engagiert, begleitet von übermäßigen Abonnement-Erinnerungen, Warenkorb-Benachrichtigungen und Zahlungsausfall-Warnungen. Diese systematische Flut widersprüchlicher Mitteilungen erzeugt unzulässigen Druck auf den Verbraucher. Darüber hinaus behält der Händler weiterhin Verbrauchermittel ein, wobei Rückerstattungen als „bevorstehend" bezeichnet werden (z.B. erwartet am 6. Februar), was ein wiederkehrendes Muster der Mitteleinbehaltung demonstriert, das die aggressive Geschäftspraxis weiter verschärft."""
    },
    "§ 433 BGB - Material Breach": {
        "law_code": "§ 433 BGB",
        "title": "Wesentliche Vertragsverletzung (Mangelhafte Lieferung)",
        "description": "Ein Teil der gelieferten Waren entsprach nicht den handelsüblichen Qualitätsstandards, einschließlich: verdorbener Milchprodukte, Artikel, die mit nicht identifizierten schwarzen Klebstoffen kontaminiert waren, und etwa fünf Pakete mit durchstochener oder beschädigter Verpackung. Obwohl diese mangelhaften Artikel eine Minderheit der Gesamtlieferung darstellen, stellen sie dennoch wesentliche Vertragsverletzungen gemäß § 433 BGB dar (Verpflichtung zur Lieferung von Waren handelsüblicher Qualität). § 433 Abs. 1 Satz 2 BGB bestimmt, dass die Sache frei von Sach- und Rechtsmängeln sein muss. Der Verkäufer hat seine Pflicht zur Lieferung mangelfreier Waren verletzt. Der Verbraucher behält sich das Recht vor, Rechtsbehelfe für diese Verletzungen geltend zu machen, vorbehaltlich der Erfüllung der vereinbarten Abonnementbedingungen und Lieferverpflichtungen durch den Händler."
    },
}

# Page copy: overview (markdown bullet list), stats labels
OVERVIEW_DE_EU = """
This complaint documents multiple violations of consumer protection laws:

- **Undisclosed fees** imposed after payment completion (violation of price transparency requirements under § 312j BGB)
- **Quality deficiencies** in delivered products and breach of delivery obligations
- **Misleading commercial practices** through material omissions regarding total costs
- **Contractual breaches** and unauthorized charges
- **Aggressive commercial practices** through systematic patterns of repetitive order confirmations and cancellations, coupled with excessive communications (subscription reminders, abandoned cart notifications, payment alerts) creating undue pressure on the consumer (documented in evidence below)

Each claim is supported by detailed legal analysis, documentary evidence, and applicable statutory references.
"""

OVERVIEW_DE = """
Diese Beschwerde dokumentiert mehrere Verstöße gegen Verbraucherschutzgesetze:

- **Nicht offengelegte Gebühren** nach Zahlungsabschluss erhoben (Verstoß gegen Preistransparenzpflichten gemäß § 312j BGB)
- **Qualitätsmängel** bei gelieferten Produkten und Verletzung von Lieferverpflichtungen
- **Irreführende Geschäftspraktiken** durch wesentliche Auslassungen bezüglich der Gesamtkosten
- **Vertragsverletzungen** und unberechtigte Forderungen
- **Aggressive Geschäftspraktiken** durch systematische Muster wiederholter Bestellbestätigungen und Stornierungen, verbunden mit übermäßigen Mitteilungen (Abonnement-Erinnerungen, Warenkorb-Benachrichtigungen, Zahlungswarnungen), die unzulässigen Druck auf den Verbraucher erzeugen (dokumentiert in den nachstehenden Beweisen)

Jede Anspruchsgrundlage wird durch detaillierte Rechtsanalyse, dokumentarische Beweise und anwendbare gesetzliche Verweise gestützt.
"""

OVERVIEW_PT = """
Esta denúncia documenta múltiplas violações das leis de proteção do consumidor:

- **Taxas não divulgadas** impostas após conclusão do pagamento (violação dos requisitos de transparência de preços ao abrigo do DL 24/2008)
- **Deficiências de qualidade** nos produtos entregues e incumprimento de obrigações de entrega
- **Práticas comerciais enganosas** através de omissões materiais relativas aos custos totais
- **Incumprimentos contratuais** e cobranças não autorizadas
- **Práticas comerciais agressivas** através de padrões sistemáticos de confirmações e cancelamentos repetitivos de encomendas, conjugados com comunicações excessivas (lembretes de subscrição, notificações de carrinho abandonado, alertas de pagamento) criando pressão indevida sobre o consumidor (documentado na prova abaixo)

Cada alegação é suportada por análise jurídica detalhada, prova documental e referências legais aplicáveis.
"""

STATS_DE_EU = {
    "applicable_law": "German Civil Code (BGB), Act Against Unfair Competition (UWG), EU Directives",
    "jurisdiction": "Federal Republic of Germany / European Union",
}
STATS_DE = {
    "applicable_law": "Bürgerliches Gesetzbuch (BGB), Gesetz gegen den unlauteren Wettbewerb (UWG), EU-Richtlinien",
    "jurisdiction": "Bundesrepublik Deutschland / Europäische Union",
}
STATS_PT = {
    "applicable_law": "DL 24/2008, DL 57/2008, DL 446/85, DL 84/2021, Código Civil Português",
    "jurisdiction": "República Portuguesa / União Europeia",
}

# Labels for expandable claim component (EN / PT)
LABELS_DE_EU = {
    "judicial_context": "JUDICIAL CONTEXT",
    "technical_proof": "TECHNICAL PROOF",
    "photo": "PHOTO",
    "comms_excerpt": "COMMS EXCERPT",
    "document_proof": "DOCUMENT PROOF",
    "voice_call_record": "VOICE CALL RECORD",
    "legal_basis": "Legal basis",
    "download": "Download",
    "preview_not_available": "Preview not available for this file type.",
    "file_not_found": "File not found.",
    "screenshots": "Screenshots",
    "documents": "Documents",
    "communications": "Communications",
    "no_evidence": "No evidence attached.",
    "previous": "Previous",
    "next": "Next",
    "of": "of",
    "add_file": "Add file",
    "source": "Source",
}
LABELS_DE = {
    "judicial_context": "RECHTLICHER KONTEXT",
    "technical_proof": "TECHNISCHER BEWEIS",
    "photo": "FOTO",
    "comms_excerpt": "KOMMUNIKATIONSAUSZUG",
    "document_proof": "DOKUMENTARISCHER BEWEIS",
    "voice_call_record": "TELEFONANRUF-PROTOKOLL",
    "legal_basis": "Rechtsgrundlage",
    "download": "Herunterladen",
    "preview_not_available": "Vorschau für diesen Dateityp nicht verfügbar.",
    "file_not_found": "Datei nicht gefunden.",
    "screenshots": "Bildschirmfotos",
    "documents": "Dokumente",
    "communications": "Kommunikationen",
    "no_evidence": "Keine Beweise beigefügt.",
    "previous": "Zurück",
    "next": "Weiter",
    "of": "von",
    "add_file": "Datei hinzufügen",
    "source": "Quelle",
}
LABELS_PT = {
    "judicial_context": "CONTEXTO JUDICIAL",
    "technical_proof": "PROVA TÉCNICA",
    "photo": "FOTO",
    "comms_excerpt": "EXCERTO DE COMUNICAÇÕES",
    "document_proof": "PROVA DOCUMENTAL",
    "voice_call_record": "REGISTO DE CHAMADA",
    "legal_basis": "Base legal",
    "download": "Descarregar",
    "preview_not_available": "Pré-visualização não disponível para este tipo de ficheiro.",
    "file_not_found": "Ficheiro não encontrado.",
    "screenshots": "Capturas de ecrã",
    "documents": "Documentos",
    "communications": "Comunicações",
    "no_evidence": "Nenhuma prova anexada.",
    "previous": "Anterior",
    "next": "Próximo",
    "of": "de",
    "add_file": "Adicionar ficheiro",
    "source": "Fonte",
}

def get_overview(locale):
    if locale == "pt":
        return OVERVIEW_PT
    elif locale == "de":
        return OVERVIEW_DE
    else:
        return OVERVIEW_DE_EU

def get_stats(locale):
    if locale == "pt":
        return STATS_PT
    elif locale == "de":
        return STATS_DE
    else:
        return STATS_DE_EU

def get_labels(locale):
    if locale == "pt":
        return LABELS_PT
    elif locale == "de":
        return LABELS_DE
    else:
        return LABELS_DE_EU

def get_violation_data_for_locale(violation_key, locale):
    """Return violation_data (law_code, title, description, evidence) for the given locale."""
    from data.evidence_mapping import EVIDENCE_MAP
    base = EVIDENCE_MAP[violation_key]
    if locale == "pt" and violation_key in TEXTS_PT:
        return {**base, **TEXTS_PT[violation_key]}
    elif locale == "de" and violation_key in TEXTS_DE:
        return {**base, **TEXTS_DE[violation_key]}
    return base
