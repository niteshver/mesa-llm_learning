                 ┌────────────────────────┐
                 │      START SYSTEM      │
                 └─────────────┬──────────┘
                               ↓
               ┌────────────────────────────────┐
               │  INITIALIZE CITY (Mesa Model)  │
               │  • Zones (A/B/C)               │
               │  • Population                  │
               │  • Water / Energy / Waste      │
               │  • Traffic / Pollution Agents  │
               └─────────────────┬──────────────┘
                                 ↓
               ┌────────────────────────────────┐
               │  RUN SIMULATION STEP (Mesa)     │
               │  • Agents Act (use resources)   │
               │  • Pollution Increases/Decreases│
               │  • Water Usage / Energy Load    │
               │  • Waste Accumulation           │
               └─────────────────┬──────────────┘
                                 ↓
               ┌────────────────────────────────┐
               │   COLLECT CITY DATA (Metrics)   │
               │   • AQI, Traffic, Water Stress  │
               │   • Energy Load, Waste Overflow │
               │   • Cost / Budget Usage         │
               └─────────────────┬──────────────┘
                                 ↓
          ┌────────────────────────────────────────────┐
          │ SEND DATA TO AI (LangChain / OpenAI GPT)    │
          │ Prompt: "Suggest optimal policies based on: │
          │  <City Metrics> under limited budget."      │
          └────────────────────┬────────────────────────┘
                                ↓
        ┌──────────────────────────────────────────────┐
        │ RECEIVE AI RECOMMENDATIONS (JSON FORMAT)      │
        │  • Traffic policies                           │
        │  • Water conservation                         │
        │  • Energy optimization                        │
        │  • Waste management                           │
        │  • Pollution control                          │
        └────────────────────┬──────────────────────────┘
                              ↓
       ┌───────────────────────────────────────────────┐
       │ APPLY POLICIES BACK INTO MESA MODEL            │
       │ • Adjust agents/resources                      │
       │ • Change vehicle numbers / factories / bins    │
       │ • Install solar / harvesting / eco rules       │
       └────────────────────┬──────────────────────────┘
                             ↓
           ┌────────────────────────────────────────┐
           │ RUN NEXT SIMULATION CYCLE (Repeat Loop)│
           └────────────────────┬───────────────────┘
                                 ↓
                     ┌───────────────────────┐
                     │ USER SEES DASHBOARD   │
                     │ • Graphs & Heatmaps   │
                     │ • AI Suggestions       │
                     │ • Before vs After AI   │
                     └─────────────┬─────────┘
                                   ↓
                       ┌────────────────────┐
                       │  GENERATE REPORT   │
                       │ (AI Written Summary│
                       │   + Policy Impact) │
                       └───────────┬────────┘
                                   ↓
                         ┌────────────────┐
                         │     END        │
                         └────────────────┘
