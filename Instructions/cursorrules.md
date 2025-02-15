# Cursor Rules Document for the Centralized Event Platform

This document, labeled ".cursorrules", outlines the coding and development guidelines for building and maintaining the centralized event discovery platform for Jordan. It serves as a set of custom rules to ensure consistency, quality, and seamless collaboration across the development team using advanced tools such as ChatGPT (GPT-4), Claude AI (Anthropic’s Sonnet 3.5), and Cursor.

1.  Coding Conventions & Formatting Guidelines

• Use consistent indentation, naming conventions, and commenting standards across Django (backend) and React-Native (frontend). • Prioritize clarity: every function and method should have a clear purpose and documentation. • Follow best practices for modular design, ensuring that components are reusable and maintainable.

1.  Tech Stack & Tool Integration

• Backend: Django framework must be organized following separation of concerns (models, views, controllers, and RESTful APIs) along with robust testing and security measures. • Frontend: The React-Native code should be structured to support a mobile-first responsive design while remaining adaptable for future native app development. • Tools such as ChatGPT, Claude AI, and Cursor should be used for code generation, error checking, and real-time code suggestions. Always review AI-generated suggestions for consistency with our custom rules.

1.  Feature Implementation & Code Architecture

• Event Management Module: Create clear interfaces for event creation, edition, and deletion. Organizers must be able to upload event details, manage schedules, and monitor performance analytics. • Ticketing System: Implement a secure ticketing flow for both free and paid events. Integration with multiple payment options (card via API, cash at event, and Cliq) must enforce PCI-DSS compliance. • User Registration & Authentication: Build a robust authentication system using OAuth, email, and phone sign-ups. Ensure that multilingual support (Arabic and English) is embedded at every step.

1.  Security & Data Privacy Standards

• Payment processes must strictly adhere to PCI-DSS standards. Build encryption and secure storage protocols within the Django backend. • Regular security audits and code reviews should be scheduled to ensure compliance with global data protection standards (including GDPR where applicable). • Implement error handling and fallback mechanisms, particularly for digital payment integrations and geolocation-based features.

1.  Responsive Design & Mobile-First Principles

• The platform must start as a responsive web application optimized for mobile devices. Use a mobile-first approach in designing the UI/UX. • Ensure compatibility across different screen sizes (smartphones, tablets, desktops) with intuitive navigation and interactive elements such as map views for event discovery.

1.  Push Notifications, Reminders & Analytics

• Incorporate a highly customizable notification system: allow users to select the frequency (instant, daily, weekly) and type (push notifications and email) of communications based on user interests and behaviors. • Analytics modules for event organizers should provide clear metrics such as ticket sales, engagement rates, demographics, CTR, and feedback scores. Present these data points in an easily digestible dashboard.

1.  Multilingual Content & Automated/Manual Translation

• All UI elements and static content should be manually curated in both Arabic and English to ensure cultural relevance; user-generated content may utilize automated translation tools with moderation. • Maintain separate resource files for different languages, ensuring that dynamic content reflects these dual languages consistently.

1.  Administrative and Moderation Controls

• Develop robust administrative tools that allow platform administrators to manage system operations, user permissions, and oversee the payment processes. • Moderation tools should be in place to verify event listings and manage user-generated content. Content guidelines and case resolution procedures must be clear and documented.

1.  Third-Party Integration & API Management

• All API integrations (payment gateways, geolocation services, social media, and email marketing tools like Mailchimp) must be handled with proper error checking and logging. • Design fallback strategies for external API downtime, ensuring alternative methods (e.g., cash payments) are gracefully integrated.

1.  Testing, Deployment, & Future Scalability

• Involve comprehensive testing cycles including unit, integration, and user-acceptance tests. Use automated testing tools wherever possible. • Deploy CI/CD pipelines with rigorous monitoring and performance-check routines to maintain high uptime and system reliability. • The codebase must be prepared for scalability. As user load and feature complexity grow, consider refactoring modules and optimizing performance.

## Conclusion

This custom .cursorrules document is essential for ensuring that the development process remains consistent with the project’s core objectives, quality standards, and technical requirements. All team members must familiarize themselves with these guidelines and adhere to them throughout the company’s development lifecycle. Continued collaboration between developers, code reviewers, and tool integrations will ensure that the platform evolves securely and efficiently while delivering a superior user experience.

End of .cursorrules Document
