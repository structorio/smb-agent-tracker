import json
V="2026-10-16"
rows=[
# id,name,url,job,tier,start,diff,who,pricing_source,verified
("booke","Booke AI","https://booke.ai","bookkeeping","Paid","$129/business/mo","easy","Owners tired of categorizing bank feed transactions by hand.","https://booke.ai/pricing",1),
("docyt","Docyt","https://docyt.com","bookkeeping","Paid","From $299/property/mo (Accounting Suite)","medium","Multi-location operators (hospitality, franchises) that need daily reconciled books.","https://docyt.com/pricing",1),
("digits","Digits","https://digits.com","bookkeeping","Paid","$65/mo (Essentials)","easy","Solopreneurs and startups wanting AI-run books and live financials.","https://digits.com/pricing",1),
("quickbooks","QuickBooks Online (Intuit Assist)","https://quickbooks.intuit.com","bookkeeping","Paid","Unverified","easy","Businesses already on QuickBooks who want built-in AI help.","https://quickbooks.intuit.com/pricing/",0),
("reclaim","Reclaim.ai","https://reclaim.ai","scheduling","Freemium","$10/seat/mo (Starter)","easy","Small teams protecting focus time and auto-scheduling tasks on Google/Outlook calendars.","https://reclaim.ai/pricing",1),
("motion","Motion","https://www.usemotion.com","scheduling","Paid","Unverified","medium","Owners who want an AI planner that schedules tasks and projects automatically.","https://www.usemotion.com/pricing",0),
("calendly","Calendly","https://calendly.com","scheduling","Freemium","$10/seat/mo (Standard)","easy","Anyone booking client meetings without back-and-forth emails.","https://calendly.com/pricing",1),
("gohighlevel","HighLevel","https://www.gohighlevel.com","lead follow-up","Paid","$97/mo (Starter), 14-day trial","hard","Agencies and service businesses wanting CRM, texting and automated follow-up in one place.","https://www.gohighlevel.com/pricing",1),
("podium","Podium","https://www.podium.com","lead follow-up","Paid","Unverified (quote-based)","medium","Local service businesses handling leads, texts and reviews.","https://www.podium.com/pricing/",0),
("smithai","Smith.ai AI Receptionist","https://smith.ai","lead follow-up","Freemium","$0 (25 calls/mo); Pro $150/mo","easy","Firms that miss calls and want every lead answered and qualified.","https://smith.ai/pricing/ai-receptionist",1),
("hubspot","HubSpot (Breeze AI)","https://www.hubspot.com","lead follow-up","Freemium","Unverified","medium","Growing businesses wanting a CRM with AI-assisted follow-up.","https://www.hubspot.com/pricing/marketing",0),
("intercom","Intercom Fin","https://www.intercom.com","customer support","Paid","$0.99/Fin outcome + from $19/seat/mo","medium","Online businesses that want an AI agent resolving support chats.","https://www.intercom.com/pricing",1),
("tidio","Tidio (Lyro)","https://www.tidio.com","customer support","Freemium","Unverified (Premium $300/mo listed)","easy","Small e-commerce shops adding live chat plus an AI chatbot.","https://www.tidio.com/pricing/",0),
("gorgias","Gorgias","https://www.gorgias.com","customer support","Paid","$40/mo (helpdesk + AI Agent starter)","medium","Shopify and e-commerce brands automating order and return questions.","https://www.gorgias.com/pricing",1),
("chatbase","Chatbase","https://www.chatbase.co","customer support","Paid","$32/mo billed yearly ($40 monthly, Hobby)","easy","Businesses training a website chatbot on their own docs and FAQs.","https://www.chatbase.co/pricing",1),
("zendesk","Zendesk","https://www.zendesk.com","customer support","Paid","$19/agent/mo paid yearly","medium","Teams outgrowing a shared inbox that want AI agents later.","https://www.zendesk.com/pricing/",1),
("bland","Bland AI","https://www.bland.ai","sales calls","Usage","$0.14/min, $0 platform fee","hard","Developers building custom AI phone agents for inbound or outbound calls.","https://www.bland.ai/pricing",1),
("synthflow","Synthflow","https://synthflow.ai","sales calls","Paid","Unverified for SMB (enterprise from $30k/yr)","medium","Businesses wanting no-code AI voice agents for calls.","https://synthflow.ai/pricing",0),
("retell","Retell AI","https://www.retellai.com","sales calls","Usage","Pay as you go, $0.07-$0.31/min, $10 free credits","hard","Builders creating AI voice agents for booking and qualification calls.","https://www.retellai.com/pricing",1),
("goodcall","Goodcall","https://www.goodcall.com","sales calls","Paid","$79/mo (Starter)","easy","Solo operators and shops that want an AI agent answering the phone.","https://www.goodcall.com/pricing",1),
("rosie","Rosie","https://heyrosie.com","sales calls","Paid","$49/mo (Professional), 7-day trial","easy","Solo owners and home-service pros who miss calls on the job.","https://heyrosie.com/pricing",1),
("fireflies","Fireflies.ai","https://fireflies.ai","sales calls","Freemium","Free; Pro $10/seat/mo billed annually","easy","Teams that want sales and client calls recorded, transcribed and summarized.","https://fireflies.ai/pricing",1),
("otter","Otter.ai","https://otter.ai","sales calls","Freemium","Pro $16.99/user/mo ($8.33 billed annually)","easy","Anyone needing meeting notes and action items automatically.","https://otter.ai/pricing",1),
("mailchimp","Mailchimp","https://mailchimp.com","marketing/email","Freemium","Unverified","easy","Small businesses sending newsletters and simple email automations.","https://mailchimp.com/pricing/marketing/",0),
("klaviyo","Klaviyo","https://www.klaviyo.com","marketing/email","Freemium","Unverified","medium","E-commerce brands running AI-assisted email and SMS campaigns.","https://www.klaviyo.com/pricing",0),
("jasper","Jasper","https://www.jasper.ai","marketing/email","Paid","Pro $59/mo billed yearly ($69 monthly)","easy","Marketers producing on-brand copy, posts and campaigns quickly.","https://www.jasper.ai/pricing",1),
("zapier","Zapier (Agents)","https://zapier.com","admin","Freemium","Free; Professional from $19.99/mo","medium","Owners connecting their apps and building AI automations without code.","https://zapier.com/pricing",1),
("make","Make","https://www.make.com","admin","Freemium","Unverified","hard","Tinkerers building complex multi-step automations visually.","https://www.make.com/en/pricing",0),
("lindy","Lindy","https://www.lindy.ai","admin","Paid","$49.99/mo (5,000 credits); $50 free credits to start","medium","Owners wanting an AI assistant for inbox, meetings and follow-ups.","https://www.lindy.ai/pricing",1),
("notion","Notion AI","https://www.notion.com","admin","Freemium","Free; Business (with AI) $20/member/mo","easy","Teams keeping docs, SOPs and projects in one AI-searchable workspace.","https://www.notion.com/pricing",1),
]
out=[dict(id=r[0],name=r[1],url=r[2],job=r[3],price_tier=r[4],starting_price=r[5],difficulty=r[6],who=r[7],pricing_source=r[8],pricing_verified=bool(r[9]),last_checked=V) for r in rows]
json.dump(out,open("data/tools.json","w"),indent=1)
open("data/tools.js","w").write("window.TOOLS="+json.dumps(out)+";")
print(len(out),sum(o["pricing_verified"] for o in out))
