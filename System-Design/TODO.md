# TODO (SYSTEM DESIGN)

## Design a Content Moderation System

Core Function: A core component of TikTok's trust and safety efforts.
CDN Implications: Systems for moderating video content impact scalability and performance requirements of the distribution network.

## Detecting DDoS Attacks

Security: Proactive DDoS mitigation is crucial for a healthy CDN infrastructure.
Trust & Safety Tie-In: DDoS attacks can disrupt service and be used to mask content moderation bypass attempts.
Design a Microservices Architecture

Modularity: Allows for dedicated microservices focusing on specific trust and safety areas (e.g., image analysis, text classification, rule-based detection) promoting better team ownership.
CDN Scale: A microservices architecture allows different trust and safety components to scale independently based on the CDN's traffic patterns.
Medium Relevance

## Design a Recommendation System

User Experience: Safe and appropriate recommendations play into trust and safety by avoiding harmful or misleading content promotion.
Indirect Relation: Less directly connected to the core mechanics of a CDN, but has trust and safety considerations impacting the network.
Consistent Hashing

Distribution: Important for cache management and load balancing in a CDN.
Focus: This leans more towards general CDN efficiency rather than being a core trust and safety requirement.
Load Balancing

Performance: Ensuring optimal load distribution impacts the user experience, which is relevant for upholding trust and safety standards.
Less Focused: A general backend requirement, less specific to the trust and safety specialization of the role.
Lower Relevance

## Design a URL Shortening Service

Functionality: While URL shortening has uses in content sharing, it is less tied to the backend trust and safety systems you're likely to design for the CDN.
Design a Rate Limiter

Useful Tool: Important for API stability and potential abuse protection.
Peripheral: Has less direct impact on the core trust and safety elements you'd likely focus on with a CDN.
