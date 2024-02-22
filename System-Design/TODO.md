# SYSTEM DESIGN

## High Relevance

### Design a Content Moderation System

- Core Function: A core component of TikTok's trust and safety efforts.
- CDN Implications: Systems for moderating video content impact scalability and performance requirements of the distribution network.
- How would you design a content moderation system to detect and filter inappropriate content on TikTok?
- Discuss approaches such as keyword filtering, machine learning-based classification, and human review workflows.
- Consider scalability, accuracy, and handling of evolving content trends.

### Detecting DDoS Attacks

- Security: Proactive DDoS mitigation is crucial for a healthy CDN infrastructure.
- Trust & Safety Tie-In: DDoS attacks can disrupt service and be used to mask content moderation bypass attempts.

### Design a Microservices Architecture

- Modularity: Allows for dedicated microservices focusing on specific trust and safety areas (e.g., image analysis, text classification, rule-based detection) promoting better team ownership.
- CDN Scale: A microservices architecture allows different trust and safety components to scale independently based on the CDN's traffic patterns.
- How would you design TikTok's backend using a microservices architecture?
- Discuss decomposition into services, communication patterns (e.g., REST, gRPC), service discovery, and fault tolerance.
- Consider trade-offs between microservices and monolithic architectures, scalability, and operational complexity.

## Medium Relevance

### Design a Recommendation System

- User Experience: Safe and appropriate recommendations play into trust and safety by avoiding harmful or misleading content promotion.
- Indirect Relation: Less directly connected to the core mechanics of a CDN, but has trust and safety considerations impacting the network.
- How would you design a recommendation system for recommending videos to TikTok users?
- Discuss user profiling, content tagging, collaborative filtering, and personalised recommendations.
- Consider scalability, real-time updates, and balancing between relevance and diversity.

### Consistent Hashing

- Distribution: Important for cache management and load balancing in a CDN.
- Focus: This leans more towards general CDN efficiency rather than being a core trust and safety requirement.

### Load Balancing

- Performance: Ensuring optimal load distribution impacts the user experience, which is relevant for upholding trust and safety standards.
- Less Focused: A general backend requirement, less specific to the trust and safety specialization of the role.

## Lower Relevance

### Design a URL Shortening Service

- Functionality: While URL shortening has uses in content sharing, it is less tied to the backend trust and safety systems you're likely to design for the CDN.
- How would you design a service like Bitly or TinyURL that shortens long URLs?
- Discuss the architecture, including components like the URL shortening algorithm, storage, and handling redirections.
- Consider scalability, fault tolerance, and performance requirements.

### Design a Rate Limiter

- Useful Tool: Important for API stability and potential abuse protection.
- Peripheral: Has less direct impact on the core trust and safety elements you'd likely focus on with a CDN.

### Design a Chat Messaging System

- How would you architect a chat messaging system similar to WhatsApp or Facebook Messenger?
- Discuss the components such as message storage, message delivery, presence indication, and notifications.
- Consider real-time requirements, scalability, and handling of concurrent users.

### Design a Content Delivery Network (CDN)

- How would you design a CDN to efficiently deliver TikTok videos to users worldwide?
- Discuss edge server placement, caching strategies, content replication, and request routing algorithms.
- Consider latency reduction, scalability, and handling of varying network conditions.

### Design an Analytics Platform

- How would you design an analytics platform to track user engagement and content performance on TikTok?
- Discuss data collection, storage (e.g., data warehousing, NoSQL databases), processing (e.g., batch processing, stream processing), and visualisation.
- Consider scalability, real-time analytics, and privacy concerns.
