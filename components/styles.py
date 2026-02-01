# Modern, Clean UI Theme
def get_styles():
    """Return a modern, user-friendly theme optimized for readability"""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --primary-blue: #2563eb;
            --primary-blue-light: #3b82f6;
            --primary-blue-dark: #1e40af;
            --success-green: #10b981;
            --warning-amber: #f59e0b;
            --danger-red: #ef4444;
            --neutral-50: #f8fafc;
            --neutral-100: #f1f5f9;
            --neutral-200: #e2e8f0;
            --neutral-300: #cbd5e1;
            --neutral-700: #334155;
            --neutral-800: #1e293b;
            --neutral-900: #0f172a;
        }

        /* Clean Base */
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        /* Sidebar - Modern & Clean */
        [data-testid="stSidebar"] {
            background: white !important;
            border-right: 1px solid var(--neutral-200);
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.04);
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1 {
            font-size: 1.5rem !important;
            margin-bottom: 0.5rem !important;
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
            font-size: 0.75rem !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--neutral-700) !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.5rem !important;
        }

        /* Typography - Clear & Readable */
        h1 {
            color: var(--neutral-900) !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.5rem !important;
            line-height: 1.2 !important;
        }
        
        h2 {
            color: var(--neutral-800) !important;
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
        }
        
        h3 {
            color: var(--neutral-800) !important;
            font-size: 1.125rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.75rem !important;
        }
        
        p, span, label {
            color: var(--neutral-700);
            line-height: 1.6;
        }

        /* Metrics - Bold & Clear */
        [data-testid="stMetricValue"] {
            color: var(--primary-blue) !important;
            font-weight: 700 !important;
            font-size: 1.875rem !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: var(--neutral-700) !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
        }

        /* Cards - Clean with Shadow */
        [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--neutral-200);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            margin-bottom: 1rem;
        }

        /* Expanders - Simplified */
        .streamlit-expanderHeader {
            background-color: white !important;
            color: var(--neutral-900) !important;
            border: 1px solid var(--neutral-200) !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
            font-size: 0.95rem !important;
            padding: 0.75rem 1rem !important;
        }
        
        .streamlit-expanderHeader:hover {
            border-color: var(--primary-blue) !important;
            background-color: var(--neutral-50) !important;
        }
        
        .streamlit-expanderContent {
            background-color: var(--neutral-50) !important;
            border: 1px solid var(--neutral-200) !important;
            border-top: none !important;
            border-radius: 0 0 8px 8px !important;
            padding: 1rem !important;
        }

        /* Evidence images: readable size, no stretch. Max 700px wide, natural aspect ratio. */
        [data-testid="stImage"] img {
            max-width: 700px !important;
            width: auto !important;
            height: auto !important;
            object-fit: contain !important;
        }

        /* Status Badge - Modern */
        .status-badge {
            background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
            color: var(--danger-red);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: 1px solid #fca5a5;
            font-size: 0.875rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .status-badge::before {
            content: "";
            width: 8px;
            height: 8px;
            background: var(--danger-red);
            border-radius: 50%;
            display: inline-block;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Tabs - Clean Pills */
        .stTabs [data-baseweb="tab-list"] {
            background-color: var(--neutral-100);
            padding: 0.25rem;
            border-radius: 10px;
            gap: 0.25rem;
            border: none;
        }

        .stTabs [data-baseweb="tab"] {
            height: 42px;
            border-radius: 8px;
            color: var(--neutral-700);
            padding: 0 1.25rem;
            font-weight: 500;
            border: none;
        }

        .stTabs [aria-selected="true"] {
            background-color: white;
            color: var(--primary-blue);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        /* Buttons - Primary Action Style */
        .stDownloadButton button, .stButton button {
            border-radius: 8px !important;
            border: 1px solid var(--neutral-300) !important;
            background: white !important;
            color: var(--neutral-900) !important;
            font-weight: 500 !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.2s !important;
        }

        .stDownloadButton button:hover, .stButton button:hover {
            border-color: var(--primary-blue) !important;
            background: var(--primary-blue) !important;
            color: white !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2) !important;
        }

        /* Radio Buttons - Modern Pills */
        [data-testid="stSidebar"] .stRadio > div {
            background: var(--neutral-50);
            border-radius: 8px;
            padding: 0.5rem;
        }

        [data-testid="stSidebar"] .stRadio > div > label {
            background: white;
            border: 1px solid var(--neutral-200);
            border-radius: 6px;
            padding: 0.75rem 1rem;
            margin-bottom: 0.25rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        [data-testid="stSidebar"] .stRadio > div > label:hover {
            border-color: var(--primary-blue);
            background: var(--neutral-50);
        }

        [data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-blue-light) 100%);
            border-color: var(--primary-blue-dark);
            color: white;
        }

        /* Info/Warning/Error Boxes */
        .stAlert {
            border-radius: 8px;
            border-left: 4px solid;
        }

        /* Scrollbar - Subtle */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: var(--neutral-100);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--neutral-300);
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: var(--neutral-400);
        }

        /* Custom Card Component */
        .custom-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--neutral-200);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            margin-bottom: 1rem;
            transition: all 0.3s;
        }

        .custom-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }

        /* Divider */
        hr {
            border: none !important;
            border-top: 1px solid var(--neutral-200) !important;
            margin: 2rem 0 !important;
        }
    </style>
    """
