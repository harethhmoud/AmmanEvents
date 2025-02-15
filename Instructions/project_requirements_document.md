# Project Requirements Document

## 1. Project Overview

This project is about building a centralized platform for event discovery in Jordan. It aims to bring together event organizers, attendees, and local businesses on one streamlined platform. The core idea is to allow event organizers to create and manage their events with ease, while giving attendees a hassle-free way to find events near them using geolocation and interactive map views. The platform also supports digital ticketing for both free and paid events, ensuring secure payment processes through local payment gateways, such as card processing, cash-at-event, and Cliq.

The platform is being created to solve the fragmentation in the event space by providing a single, user-friendly solution that caters to today’s diverse audience. Key objectives include seamless event discovery, straightforward ticketing with secure payments (complying with PCI-DSS), and robust event management tools for organizers which include basic analytics and effective marketing. Success will be measured by high user engagement, increased ticket sales, and positive feedback from both organizers and attendees.

## 2. In-Scope vs. Out-of-Scope

**In-Scope:**

*   Event Creation & Management: Comprehensive tools for event organizers to create and manage events.
*   Dual Views: Separate vendor and customer views.
*   Ticketing System: Support for free and paid events with digital payments (including card payments via API, cash options at events, and Cliq).
*   User Registration & Authentication: Multiple sign-up methods including OAuth, email, and phone-based authentication.
*   Event Discovery & Search: Filters using keywords, categories, and geolocation features with interactive map views.
*   Wishlist & Save for Later: Users can bookmark events they are interested in.
*   Push Notifications and Email Reminders: Personalized alerts with selectable frequency options (instant, daily, weekly) triggered by user interests and event updates.
*   Bilingual Support: Arabic and English language support with manual translations for UI and static content and automated tools for user-generated content.
*   Basic Organizer Analytics: Key metrics such as ticket sales, engagement rates, demographics, CTR, and feedback scores.
*   Mobile-First Responsive Design: A responsive web app optimized for mobile devices, tablets, and desktops.
*   Administrative & Moderation Tools: Backend modules for platform administrators and moderators to manage system operations, user permissions, and content moderation.
*   Third-Party Integrations: Social media sharing integrations (Facebook, Instagram, Twitter) and email marketing tools (like Mailchimp).

**Out-of-Scope:**

*   Native Mobile Applications: Direct native app development for iOS/Android is deferred to later phases.
*   Detailed Design and Branding Guidelines: Visual elements, logos, and detailed color schemes to be developed later.
*   Advanced Analytical Tools Beyond Basic Metrics: For now, only essential analytics for event performance will be developed.
*   Extended Third-Party Integrations: Beyond the basics (social media sharing and email marketing), additional integrations are planned for future iterations.
*   Comprehensive automated translation systems: While some automated translation for user-generated content will be implemented, critical UI components will rely on manual translation for cultural accuracy.

## 3. User Flow

A new user who visits the platform will first encounter a sign-up page where they can register using either OAuth, email, or phone authentication. Upon choosing their preferred language (Arabic or English), they complete the registration process quickly and are then directed to a personalized dashboard. This dashboard provides an overview of upcoming events, their wishlist, and options to update their profile. The layout is designed with a mobile-first approach, ensuring a smooth and intuitive experience across all devices.

As users navigate through the platform, they can easily discover events by searching with keywords, filtering by categories, or using geolocation features which not only filter events by proximity but also visualize them on a map view. After selecting an event, users are presented with detailed information including event schedules, venue details, ticketing options, and organizer data. They can directly purchase tickets through secure payment integrations or choose to save the event for later. Additionally, push notifications and email alerts, personalized to user preferences, keep users informed about upcoming events and purchase status changes.

## 4. Core Features (Bullet Points)

*   **Event Creation & Management:**

    *   Tools for organizers to create, edit, and manage events.
    *   Separate views for vendors and customers to distinguish between organizer and attendee needs.

*   **Ticketing System:**

    *   Support for both free and paid events.
    *   Integrated digital payments that include card payments via API, cash payment options at events, and payment through Cliq.
    *   Strict adherence to PCI-DSS standards for security.

*   **User Registration & Authentication:**

    *   Multiple sign-up methods (OAuth, Email, Phone).
    *   Secure login and account management processes.

*   **Event Discovery & Search:**

    *   Filtering options such as categories, keywords, and geolocation (proximity filtering and map views).
    *   Option for users to bookmark and save events for later.

*   **Notifications & Reminders:**

    *   Personalized push notifications and email reminders triggered by events of interest and updates.
    *   Options for users to set the frequency (instant, daily, weekly) and customize their notifications.

*   **Bilingual Support:**

    *   Dual language support for Arabic and English.
    *   Manual curation for UI and static content with automated translation for user-generated content as needed.

*   **Analytics for Organizers:**

    *   Basic analytics dashboard displaying key metrics: ticket sales, revenue trends, engagement rates, CTR, demographic breakdown, and post-event feedback.

*   **Administrative and Moderation Tools:**

    *   Administrative controls for managing overall system operations, user permissions, and payment processes.
    *   Moderation tools for content management and issue resolution.

*   **Third-Party Integrations:**

    *   Social media sharing (Facebook, Instagram, Twitter) for event promotion.
    *   Integration with email marketing tools like Mailchimp.

*   **Mobile-First Responsive Design:**

    *   Optimized for smartphones, tablets, and desktops ensuring a seamless user experience.

## 5. Tech Stack & Tools

*   **Frontend Framework:**

    *   Responsive web app built with React-Native (with future adaptations toward native mobile apps if needed).

*   **Backend Framework:**

    *   Django for server-side logic and API management.

*   **Authentication:**

    *   OAuth integration along with email and phone-based registration systems.

*   **Payment Gateways:**

    *   Integration through secure APIs supporting card payments, cash payment at events, and Cliq.

*   **Languages & Libraries:**

    *   English and Arabic language support with both manual translations for critical UI elements and automated translations for dynamic content.

*   **AI & Code Assistance Tools:**

    *   ChatGPT (GPT-4 O1 model) for advanced code generation.
    *   Claude AI (Anthropic's Sonnet 3.5 model) for intelligent code assistance.
    *   Cursor as an advanced IDE for real-time coding suggestions.

*   **Monitoring & Analytics:**

    *   Basic analytics tools integrated on the organizer dashboard to track key metrics.

*   **Third-Party Integrations:**

    *   Social media integration for event sharing.
    *   Email marketing integration (e.g., Mailchimp).

## 6. Non-Functional Requirements

*   **Performance:**

    *   Fast load times on mobile devices, ideally within 2-3 seconds per page, to accommodate mobile-first users.

*   **Security:**

    *   Strict compliance with PCI-DSS for all payment processes.
    *   Best practices for data privacy (potentially GDPR for non-local users).
    *   Secure authentication and user data storage policies.

*   **Usability:**

    *   An intuitive, mobile-first user interface that ensures a smooth experience across multiple devices.
    *   Clear visual cues and straightforward navigation for a diverse user base.

*   **Compliance & Reliability:**

    *   High uptime and reliability to support real-time event updates and ticketing.
    *   Regular security audits and compliance checks.

*   **Scalability:**

    *   Ability to accommodate an increasing number of users and events without significant delays or performance drops.

## 7. Constraints & Assumptions

*   **Constraints:**

    *   Reliance on local payment gateway APIs and adherence to specific regional payment methods (card payments, cash, Cliq).
    *   Must comply with PCI-DSS standards for payment security.
    *   The current phase is a responsive web app; native mobile apps will be considered based on future feedback.

*   **Assumptions:**

    *   The initial focus on core features for event discovery and ticketing will cover the majority of user needs.
    *   Dual language support is essential from the start, with manual curation for key UI elements.
    *   There is an expectation that user engagement with push notifications and reminders will drive better conversion rates.
    *   Tools like ChatGPT, Claude, and Cursor will be integrated smoothly into the development workflow.
    *   Future scalability requirements can be met by extending the existing tech stack when necessary.

## 8. Known Issues & Potential Pitfalls

*   **API Rate Limits and Payment Integration Issues:**

    *   Payment gateway APIs might have rate limits or intermittent outages. Implement proper error handling and fallback mechanisms (e.g., cash payment options) to mitigate potential interruptions.

*   **Geolocation Accuracy & Map View Challenges:**

    *   Ensuring precise geolocation data and a responsive map view across different devices could be challenging. Use robust map API libraries and conduct thorough testing across various devices.

*   **Bilingual Content Management:**

    *   Maintaining up-to-date and culturally relevant translations can be complex. Establish clear processes for manual translation of static content and use automated translation with moderation for dynamic content.

*   **Notification System Overload:**

    *   Over-notification could lead to user fatigue. Ensure settings are highly customizable, allowing users to control the frequency and relevance of alerts.

*   **Scalability Concerns:**

    *   As the platform grows with more users and events, performance issues could surface. Design the backend with scalability in mind and consider future migrations or optimizations.

*   **Administrative Overhead:**

    *   Balancing ease of use for administrators while keeping a secure and well-moderated system might pose challenges. Early planning for admin tools and clear content moderation guidelines will be essential.

This document serves as the comprehensive brain of the project. Every subsequent document—whether it is the Tech Stack Document, Frontend Guidelines, Backend Structure, or IDE rules—should reference this PRD to ensure all development remains aligned with the project’s core objectives and requirements.
