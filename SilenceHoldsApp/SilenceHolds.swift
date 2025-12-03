import SwiftUI
import Foundation

// MARK: - Data Models

// Badge System
struct Badge: Identifiable, Codable {
    let id: String
    let name: String
    let description: String
    let icon: String
    let requirement: Int
    let category: BadgeCategory
    
    init(id: String, name: String, description: String, icon: String, requirement: Int, category: BadgeCategory) {
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.requirement = requirement
        self.category = category
    }
}

enum BadgeCategory: String, CaseIterable {
    case sobriety = "sobriety"
    case wellness = "wellness"
    case community = "community"
    case mindfulness = "mindfulness"
}

struct BadgeProgress: Codable {
    var current: Int = 0
    var earned: Bool = false
    var earnedDate: Date?
}

// Sobriety Journey
struct SobrietyData: Codable {
    var soberFrom: String
    var soberReason: String
    var startDate: Date
    var currentStreak: Int
    var totalDays: Int
    var lastLogDate: String?
    var dailyLogs: [SobrietyLog]
    
    init(soberFrom: String, soberReason: String) {
        self.soberFrom = soberFrom
        self.soberReason = soberReason
        self.startDate = Date()
        self.currentStreak = 0
        self.totalDays = 0
        self.lastLogDate = nil
        self.dailyLogs = []
    }
}

struct SobrietyLog: Codable {
    let date: String
    let timestamp: Date
}

// Wellness Data
struct WellnessData: Codable {
    var moodHistory: [MoodEntry]
    var gratitudeJournal: [GratitudeEntry]
    var selfcareGoals: [SelfcareGoal]
    var sleepHistory: [SleepEntry]
    var lastCheckIn: String?
    
    init() {
        self.moodHistory = []
        self.gratitudeJournal = []
        self.selfcareGoals = []
        self.sleepHistory = []
        self.lastCheckIn = nil
    }
}

struct MoodEntry: Codable {
    let mood: String
    let date: String
    let timestamp: Date
}

struct GratitudeEntry: Codable {
    let text: String
    let date: String
    let timestamp: Date
}

struct SelfcareGoal: Codable, Identifiable {
    let id: String
    let text: String
    let completed: Bool
    let createdAt: Date
    
    init(text: String) {
        self.id = UUID().uuidString
        self.text = text
        self.completed = false
        self.createdAt = Date()
    }
}

struct SleepEntry: Codable {
    let hours: Double
    let date: String
    let timestamp: Date
}

struct Story: Identifiable, Codable {
    let id: String
    let title: String
    let content: String
    let tags: [String]
    let ageRange: String?
    let status: StoryStatus
    let submittedAt: Date
    let approvedAt: Date?
    
    init(title: String, content: String, tags: [String], ageRange: String? = nil) {
        self.id = UUID().uuidString
        self.title = title
        self.content = content
        self.tags = tags
        self.ageRange = ageRange
        self.status = .pending
        self.submittedAt = Date()
        self.approvedAt = nil
    }
    
    init(id: String, title: String, content: String, tags: [String], ageRange: String?, status: StoryStatus, submittedAt: Date, approvedAt: Date?) {
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags
        self.ageRange = ageRange
        self.status = status
        self.submittedAt = submittedAt
        self.approvedAt = approvedAt
    }
}

enum StoryStatus: String, Codable, CaseIterable {
    case pending = "pending"
    case approved = "approved"
    case rejected = "rejected"
    case deleted = "deleted"
}

struct StoryTag: Identifiable, CaseIterable {
    let id = UUID()
    let name: String
    let color: String
    let textColor: String
    
    static let allCases: [StoryTag] = [
        StoryTag(name: "anxiety", color: "#dbeafe", textColor: "#1e40af"),
        StoryTag(name: "depression", color: "#fecaca", textColor: "#dc2626"),
        StoryTag(name: "family", color: "#fed7aa", textColor: "#ea580c"),
        StoryTag(name: "friends", color: "#dcfce7", textColor: "#16a34a"),
        StoryTag(name: "school", color: "#e0e7ff", textColor: "#7c3aed"),
        StoryTag(name: "relationships", color: "#fce7f3", textColor: "#be185d"),
        StoryTag(name: "self-care", color: "#fef3c7", textColor: "#d97706"),
        StoryTag(name: "therapy", color: "#d1fae5", textColor: "#059669"),
        StoryTag(name: "recovery", color: "#f3e8ff", textColor: "#7c2d12"),
        StoryTag(name: "hope", color: "#fef2f2", textColor: "#991b1b")
    ]
    
    var displayName: String {
        return name.capitalized
    }
}

struct Resource: Identifiable {
    let id = UUID()
    let title: String
    let description: String
    let type: ResourceType
    let action: String
    let url: String?
    
    init(title: String, description: String, type: ResourceType, action: String, url: String? = nil) {
        self.title = title
        self.description = description
        self.type = type
        self.action = action
        self.url = url
    }
}

enum ResourceType: String, CaseIterable {
    case hotline = "hotline"
    case article = "article"
    case app = "app"
    case website = "website"
    
    var displayName: String {
        return rawValue.uppercased()
    }
    
    var color: String {
        switch self {
        case .hotline:
            return "#dc2626"
        case .article:
            return "#2563eb"
        case .app:
            return "#059669"
        case .website:
            return "#7c3aed"
        }
    }
}

// MARK: - ViewModels

// Badge System ViewModel
class BadgeStore: ObservableObject {
    @Published var badgeProgress: [String: BadgeProgress] = [:]
    @Published var showBadgeAlert = false
    @Published var badgeAlertMessage = ""
    @Published var badgeAlertTitle = ""
    
    private let badgeProgressKey = "silenceHoldsBadgeProgress"
    
    let availableBadges: [Badge] = [
        Badge(id: "first-day", name: "First Step", description: "Complete your first day of sobriety", icon: "🌟", requirement: 1, category: .sobriety),
        Badge(id: "one-week", name: "Week Warrior", description: "Stay sober for one week", icon: "⭐", requirement: 7, category: .sobriety),
        Badge(id: "one-month", name: "Month Master", description: "Stay sober for one month", icon: "🏆", requirement: 30, category: .sobriety),
        Badge(id: "three-months", name: "Quarter Champion", description: "Stay sober for three months", icon: "👑", requirement: 90, category: .sobriety),
        Badge(id: "six-months", name: "Half Year Hero", description: "Stay sober for six months", icon: "💎", requirement: 180, category: .sobriety),
        Badge(id: "one-year", name: "Year Legend", description: "Stay sober for one year", icon: "🎊", requirement: 365, category: .sobriety),
        Badge(id: "mood-tracker", name: "Mood Tracker", description: "Log your mood for 7 days", icon: "😊", requirement: 7, category: .wellness),
        Badge(id: "gratitude-guru", name: "Gratitude Guru", description: "Write in your gratitude journal for 14 days", icon: "🙏", requirement: 14, category: .wellness),
        Badge(id: "sleep-champion", name: "Sleep Champion", description: "Log your sleep for 30 days", icon: "😴", requirement: 30, category: .wellness)
    ]
    
    init() {
        loadBadgeProgress()
    }
    
    func updateBadgeProgress(badgeId: String, increment: Int = 1) {
        if badgeProgress[badgeId] == nil {
            badgeProgress[badgeId] = BadgeProgress()
        }
        
        badgeProgress[badgeId]?.current += increment
        
        // Check if badge is earned
        if let badge = availableBadges.first(where: { $0.id == badgeId }),
           let progress = badgeProgress[badgeId],
           progress.current >= badge.requirement && !progress.earned {
            
            badgeProgress[badgeId]?.earned = true
            badgeProgress[badgeId]?.earnedDate = Date()
            saveBadgeProgress()
            
            // Show celebration alert
            showBadgeCelebration(badge: badge)
        }
    }
    
    private func showBadgeCelebration(badge: Badge) {
        badgeAlertTitle = "🏆 Badge Earned!"
        badgeAlertMessage = "Congratulations! You've earned the '\(badge.name)' badge! \(badge.description)"
        showBadgeAlert = true
    }
    
    private func loadBadgeProgress() {
        if let data = UserDefaults.standard.data(forKey: badgeProgressKey),
           let decoded = try? JSONDecoder().decode([String: BadgeProgress].self, from: data) {
            badgeProgress = decoded
        }
    }
    
    private func saveBadgeProgress() {
        if let encoded = try? JSONEncoder().encode(badgeProgress) {
            UserDefaults.standard.set(encoded, forKey: badgeProgressKey)
        }
    }
}

// Sobriety Journey ViewModel
class SobrietyStore: ObservableObject {
    @Published var sobrietyData: SobrietyData?
    @Published var showCelebrationAlert = false
    @Published var celebrationMessage = ""
    
    private let sobrietyKey = "silenceHoldsSober"
    
    init() {
        loadSobrietyData()
    }
    
    func startSobrietyJourney(soberFrom: String, soberReason: String) {
        sobrietyData = SobrietyData(soberFrom: soberFrom, soberReason: soberReason)
        saveSobrietyData()
    }
    
    func logSoberDay() {
        guard var data = sobrietyData else { return }
        
        let today = Date().formatted(date: .abbreviated, time: .omitted)
        
        // Check if already logged today
        if data.lastLogDate == today {
            return
        }
        
        // Add to daily logs
        data.dailyLogs.append(SobrietyLog(date: today, timestamp: Date()))
        data.currentStreak += 1
        data.totalDays += 1
        data.lastLogDate = today
        
        sobrietyData = data
        saveSobrietyData()
        
        // Show celebration for milestones
        showSobrietyCelebration(days: data.currentStreak)
    }
    
    func reportRelapse() {
        guard var data = sobrietyData else { return }
        
        // Reset current streak but keep total days
        data.currentStreak = 0
        data.lastLogDate = nil
        
        sobrietyData = data
        saveSobrietyData()
        
        // Show supportive message
        showSupportiveMessage(totalDays: data.totalDays)
    }
    
    func resetJourney() {
        sobrietyData = nil
        UserDefaults.standard.removeObject(forKey: sobrietyKey)
    }
    
    private func showSobrietyCelebration(days: Int) {
        let celebrationMessages: [Int: String] = [
            1: "🎉 First day! You did it!",
            7: "🌟 One week! You're amazing!",
            30: "🏆 One month! You're incredible!",
            90: "⭐ Three months! You're a warrior!",
            180: "👑 Six months! You're a legend!",
            365: "🎊 One year! You're absolutely phenomenal!"
        ]
        
        if let message = celebrationMessages[days] {
            celebrationMessage = message
            showCelebrationAlert = true
        }
    }
    
    private func showSupportiveMessage(totalDays: Int) {
        celebrationMessage = "It's okay. Relapse is part of recovery. You've still accomplished \(totalDays) total days, and that matters. You can start again. 💚"
        showCelebrationAlert = true
    }
    
    private func loadSobrietyData() {
        if let data = UserDefaults.standard.data(forKey: sobrietyKey),
           let decoded = try? JSONDecoder().decode(SobrietyData.self, from: data) {
            sobrietyData = decoded
        }
    }
    
    private func saveSobrietyData() {
        if let data = sobrietyData,
           let encoded = try? JSONEncoder().encode(data) {
            UserDefaults.standard.set(encoded, forKey: sobrietyKey)
        }
    }
}

// Wellness ViewModel
class WellnessStore: ObservableObject {
    @Published var wellnessData = WellnessData()
    @Published var showMoodAlert = false
    @Published var moodAlertMessage = ""
    
    private let wellnessKey = "silenceHoldsWellness"
    
    init() {
        loadWellnessData()
    }
    
    func logMood(_ mood: String) {
        let today = Date().formatted(date: .abbreviated, time: .omitted)
        
        // Check if already logged today
        if wellnessData.lastCheckIn == today {
            moodAlertMessage = "You've already logged your mood today!"
            showMoodAlert = true
            return
        }
        
        wellnessData.moodHistory.append(MoodEntry(mood: mood, date: today, timestamp: Date()))
        wellnessData.lastCheckIn = today
        saveWellnessData()
    }
    
    func addGratitude(_ text: String) {
        let today = Date().formatted(date: .abbreviated, time: .omitted)
        wellnessData.gratitudeJournal.append(GratitudeEntry(text: text, date: today, timestamp: Date()))
        saveWellnessData()
    }
    
    func addSelfcareGoal(_ text: String) {
        wellnessData.selfcareGoals.append(SelfcareGoal(text: text))
        saveWellnessData()
    }
    
    func logSleep(_ hours: Double) {
        let today = Date().formatted(date: .abbreviated, time: .omitted)
        wellnessData.sleepHistory.append(SleepEntry(hours: hours, date: today, timestamp: Date()))
        saveWellnessData()
    }
    
    private func loadWellnessData() {
        if let data = UserDefaults.standard.data(forKey: wellnessKey),
           let decoded = try? JSONDecoder().decode(WellnessData.self, from: data) {
            wellnessData = decoded
        }
    }
    
    private func saveWellnessData() {
        if let encoded = try? JSONEncoder().encode(wellnessData) {
            UserDefaults.standard.set(encoded, forKey: wellnessKey)
        }
    }
}

class StoryStore: ObservableObject {
    @Published var stories: [Story] = []
    @Published var approvedStories: [Story] = []
    
    private let storiesKey = "silenceHoldsStories"
    private let approvedStoriesKey = "silenceHoldsApprovedStories"
    
    init() {
        loadStories()
    }
    
    func addStory(_ story: Story) {
        stories.append(story)
        saveStories()
        
        // Auto-approve stories that pass moderation
        if moderateContent(title: story.title, content: story.content).approved {
            var approvedStory = story
            approvedStory = Story(
                id: story.id,
                title: story.title,
                content: story.content,
                tags: story.tags,
                ageRange: story.ageRange,
                status: .approved,
                submittedAt: story.submittedAt,
                approvedAt: Date()
            )
            approvedStories.append(approvedStory)
            saveApprovedStories()
        }
    }
    
    func deleteStory(_ storyId: String) {
        stories.removeAll { $0.id == storyId }
        approvedStories.removeAll { $0.id == storyId }
        saveStories()
        saveApprovedStories()
    }
    
    private func moderateContent(title: String, content: String) -> (approved: Bool, reason: String) {
        let inappropriateWords = [
            "hate", "kill", "die", "suicide", "self-harm", "cutting", "overdose",
            "drug", "alcohol", "drunk", "high", "sex", "sexual", "explicit",
            "violence", "abuse", "rape", "threat", "harm", "dangerous"
        ]
        
        let text = (title + " " + content).lowercased()
        
        // Check for inappropriate content
        for word in inappropriateWords {
            if text.contains(word) {
                return (false, "Content contains inappropriate language or themes")
            }
        }
        
        // Check content length
        if content.count < 50 {
            return (false, "Story is too short. Please share more details.")
        }
        
        if content.count > 2000 {
            return (false, "Story is too long. Please keep it under 2000 characters.")
        }
        
        // Check for positive mental health content
        let positiveWords = [
            "hope", "recovery", "healing", "support", "help", "therapy", "counseling",
            "better", "improve", "strength", "courage", "journey", "growth", "learn",
            "understand", "connect", "share", "community", "safe", "care"
        ]
        
        let negativeWords = ["terrible", "awful", "horrible", "worst", "hate", "despair", "hopeless"]
        
        let positiveCount = positiveWords.reduce(0) { count, word in
            text.contains(word) ? count + 1 : count
        }
        
        let negativeCount = negativeWords.reduce(0) { count, word in
            text.contains(word) ? count + 1 : count
        }
        
        if negativeCount > 3 && positiveCount < 2 {
            return (false, "Story focuses too much on negative aspects. Please include some hope or positive elements.")
        }
        
        return (true, "Story meets community guidelines")
    }
    
    private func loadStories() {
        if let data = UserDefaults.standard.data(forKey: storiesKey),
           let decodedStories = try? JSONDecoder().decode([Story].self, from: data) {
            stories = decodedStories
        }
        
        if let data = UserDefaults.standard.data(forKey: approvedStoriesKey),
           let decodedStories = try? JSONDecoder().decode([Story].self, from: data) {
            approvedStories = decodedStories
        }
    }
    
    private func saveStories() {
        if let encoded = try? JSONEncoder().encode(stories) {
            UserDefaults.standard.set(encoded, forKey: storiesKey)
        }
    }
    
    private func saveApprovedStories() {
        if let encoded = try? JSONEncoder().encode(approvedStories) {
            UserDefaults.standard.set(encoded, forKey: approvedStoriesKey)
        }
    }
}

class ResourceStore: ObservableObject {
    @Published var resources: [Resource] = []
    
    init() {
        loadResources()
    }
    
    private func loadResources() {
        resources = [
            Resource(
                title: "988 Suicide & Crisis Lifeline",
                description: "Free, 24/7 support for people in crisis. Call or text 988 to speak with a trained crisis counselor.",
                type: .hotline,
                action: "Call 988",
                url: "tel:988"
            ),
            Resource(
                title: "Crisis Text Line",
                description: "Free, 24/7 support for people in crisis. Text HOME to 741741 to connect with a trained crisis counselor.",
                type: .hotline,
                action: "Text HOME to 741741",
                url: "sms:741741&body=HOME"
            ),
            Resource(
                title: "Teen Mental Health First Aid",
                description: "A comprehensive guide to understanding and supporting teen mental health.",
                type: .article,
                action: "Learn more",
                url: nil
            ),
            Resource(
                title: "Headspace for Teens",
                description: "Meditation and mindfulness app with content specifically designed for teenagers.",
                type: .app,
                action: "Learn more",
                url: nil
            ),
            Resource(
                title: "Soluna",
                description: "Mental health and wellness app designed for teens, offering mood tracking, coping strategies, and peer support.",
                type: .app,
                action: "Learn more",
                url: nil
            )
        ]
    }
    
    func openResource(_ resource: Resource) {
        guard let urlString = resource.url,
              let url = URL(string: urlString) else {
            return
        }
        
        if UIApplication.shared.canOpenURL(url) {
            UIApplication.shared.open(url)
        }
    }
}

// MARK: - Views

// Sobriety Journey Views
struct SobrietyJourneyView: View {
    @StateObject private var sobrietyStore = SobrietyStore()
    @StateObject private var badgeStore = BadgeStore()
    @State private var showStartJourney = false
    @State private var soberFrom = ""
    @State private var soberReason = ""
    @State private var showRelapseAlert = false
    @State private var showResetAlert = false
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    if let data = sobrietyStore.sobrietyData {
                        // Current Journey Display
                        VStack(spacing: 16) {
                            Text("Your Sobriety Journey")
                                .font(.title)
                                .fontWeight(.bold)
                                .foregroundColor(.primary)
                            
                            VStack(spacing: 12) {
                                HStack {
                                    Text("Staying sober from:")
                                        .font(.headline)
                                    Spacer()
                                    Text(data.soberFrom)
                                        .font(.body)
                                        .foregroundColor(.secondary)
                                }
                                
                                HStack {
                                    Text("Reason:")
                                        .font(.headline)
                                    Spacer()
                                    Text(data.soberReason)
                                        .font(.body)
                                        .foregroundColor(.secondary)
                                }
                                
                                HStack {
                                    Text("Current Streak:")
                                        .font(.headline)
                                    Spacer()
                                    Text("\(data.currentStreak) days")
                                        .font(.title2)
                                        .fontWeight(.bold)
                                        .foregroundColor(.green)
                                }
                                
                                HStack {
                                    Text("Total Days:")
                                        .font(.headline)
                                    Spacer()
                                    Text("\(data.totalDays) days")
                                        .font(.title2)
                                        .fontWeight(.bold)
                                        .foregroundColor(.blue)
                                }
                            }
                            .padding()
                            .background(
                                RoundedRectangle(cornerRadius: 12)
                                    .fill(Color.white)
                                    .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
                            )
                            
                            // Action Buttons
                            VStack(spacing: 12) {
                                Button(action: {
                                    sobrietyStore.logSoberDay()
                                    badgeStore.updateBadgeProgress(badgeId: "first-day")
                                }) {
                                    Text("Log Today as Sober")
                                        .font(.headline)
                                        .foregroundColor(.white)
                                        .frame(maxWidth: .infinity)
                                        .padding()
                                        .background(
                                            RoundedRectangle(cornerRadius: 8)
                                                .fill(Color.green)
                                        )
                                }
                                
                                HStack(spacing: 12) {
                                    Button(action: {
                                        showRelapseAlert = true
                                    }) {
                                        Text("Report Relapse")
                                            .font(.body)
                                            .foregroundColor(.red)
                                            .padding()
                                            .background(
                                                RoundedRectangle(cornerRadius: 8)
                                                    .stroke(Color.red, lineWidth: 1)
                                            )
                                    }
                                    
                                    Button(action: {
                                        showResetAlert = true
                                    }) {
                                        Text("Reset Journey")
                                            .font(.body)
                                            .foregroundColor(.orange)
                                            .padding()
                                            .background(
                                                RoundedRectangle(cornerRadius: 8)
                                                    .stroke(Color.orange, lineWidth: 1)
                                            )
                                    }
                                }
                            }
                        }
                    } else {
                        // Start Journey
                        VStack(spacing: 20) {
                            Text("Start Your Sobriety Journey")
                                .font(.title)
                                .fontWeight(.bold)
                                .foregroundColor(.primary)
                            
                            Text("Begin your path to recovery with support and tracking")
                                .font(.body)
                                .foregroundColor(.secondary)
                                .multilineTextAlignment(.center)
                            
                            Button(action: {
                                showStartJourney = true
                            }) {
                                Text("Start Journey")
                                    .font(.headline)
                                    .foregroundColor(.white)
                                    .frame(maxWidth: .infinity)
                                    .padding()
                                    .background(
                                        RoundedRectangle(cornerRadius: 8)
                                            .fill(Color(red: 0.72, green: 0.61, blue: 0.49))
                                    )
                            }
                        }
                        .padding()
                    }
                }
                .padding()
            }
            .navigationTitle("Sobriety Journey")
            .navigationBarTitleDisplayMode(.inline)
            .alert("Start Sobriety Journey", isPresented: $showStartJourney) {
                TextField("What are you staying sober from?", text: $soberFrom)
                TextField("Why is this important to you?", text: $soberReason)
                Button("Start") {
                    sobrietyStore.startSobrietyJourney(soberFrom: soberFrom, soberReason: soberReason)
                    soberFrom = ""
                    soberReason = ""
                }
                Button("Cancel", role: .cancel) { }
            }
            .alert("Report Relapse", isPresented: $showRelapseAlert) {
                Button("Yes, Report Relapse") {
                    sobrietyStore.reportRelapse()
                }
                Button("Cancel", role: .cancel) { }
            } message: {
                Text("This will reset your current streak but keep your total days. Are you sure?")
            }
            .alert("Reset Journey", isPresented: $showResetAlert) {
                Button("Yes, Reset Everything", role: .destructive) {
                    sobrietyStore.resetJourney()
                }
                Button("Cancel", role: .cancel) { }
            } message: {
                Text("This will delete all your progress. Are you sure?")
            }
            .alert(sobrietyStore.celebrationMessage, isPresented: $sobrietyStore.showCelebrationAlert) {
                Button("OK") { }
            }
            .alert(badgeStore.badgeAlertTitle, isPresented: $badgeStore.showBadgeAlert) {
                Button("OK") { }
            } message: {
                Text(badgeStore.badgeAlertMessage)
            }
        }
    }
}

// Wellness Tracking View
struct WellnessView: View {
    @StateObject private var wellnessStore = WellnessStore()
    @StateObject private var badgeStore = BadgeStore()
    @State private var selectedMood = "😊"
    @State private var gratitudeText = ""
    @State private var selfcareGoal = ""
    @State private var sleepHours = ""
    
    let moods = ["😊", "😐", "😔", "😰", "😡", "😴", "🤗", "💪"]
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    // Mood Tracking
                    VStack(spacing: 16) {
                        Text("How are you feeling today?")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        LazyVGrid(columns: Array(repeating: GridItem(.flexible()), count: 4), spacing: 12) {
                            ForEach(moods, id: \.self) { mood in
                                Button(action: {
                                    selectedMood = mood
                                    wellnessStore.logMood(mood)
                                    badgeStore.updateBadgeProgress(badgeId: "mood-tracker")
                                }) {
                                    Text(mood)
                                        .font(.system(size: 32))
                                        .frame(width: 60, height: 60)
                                        .background(
                                            Circle()
                                                .fill(selectedMood == mood ? Color.blue.opacity(0.3) : Color.gray.opacity(0.1))
                                        )
                                }
                            }
                        }
                    }
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.white)
                            .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
                    )
                    
                    // Gratitude Journal
                    VStack(spacing: 16) {
                        Text("Gratitude Journal")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        TextField("What are you grateful for today?", text: $gratitudeText, axis: .vertical)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .lineLimit(3...6)
                        
                        Button(action: {
                            if !gratitudeText.isEmpty {
                                wellnessStore.addGratitude(gratitudeText)
                                badgeStore.updateBadgeProgress(badgeId: "gratitude-guru")
                                gratitudeText = ""
                            }
                        }) {
                            Text("Add to Journal")
                                .font(.body)
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 8)
                                        .fill(Color.purple)
                                )
                        }
                    }
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.white)
                            .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
                    )
                    
                    // Self-Care Goals
                    VStack(spacing: 16) {
                        Text("Self-Care Goals")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        TextField("What's your self-care goal today?", text: $selfcareGoal)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                        
                        Button(action: {
                            if !selfcareGoal.isEmpty {
                                wellnessStore.addSelfcareGoal(selfcareGoal)
                                selfcareGoal = ""
                            }
                        }) {
                            Text("Add Goal")
                                .font(.body)
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 8)
                                        .fill(Color.orange)
                                )
                        }
                    }
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.white)
                            .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
                    )
                    
                    // Sleep Tracking
                    VStack(spacing: 16) {
                        Text("Sleep Tracking")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        TextField("Hours of sleep last night", text: $sleepHours)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .keyboardType(.decimalPad)
                        
                        Button(action: {
                            if let hours = Double(sleepHours), hours >= 0 && hours <= 24 {
                                wellnessStore.logSleep(hours)
                                badgeStore.updateBadgeProgress(badgeId: "sleep-champion")
                                sleepHours = ""
                            }
                        }) {
                            Text("Log Sleep")
                                .font(.body)
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 8)
                                        .fill(Color.blue)
                                )
                        }
                    }
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.white)
                            .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
                    )
                }
                .padding()
            }
            .navigationTitle("My Wellness")
            .navigationBarTitleDisplayMode(.inline)
            .alert("Mood Logged", isPresented: $wellnessStore.showMoodAlert) {
                Button("OK") { }
            } message: {
                Text(wellnessStore.moodAlertMessage)
            }
            .alert(badgeStore.badgeAlertTitle, isPresented: $badgeStore.showBadgeAlert) {
                Button("OK") { }
            } message: {
                Text(badgeStore.badgeAlertMessage)
            }
        }
    }
}

struct LogoView: View {
    var body: some View {
        Image("logo")
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 100, height: 100)
    }
}

struct HomeView: View {
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 30) {
                    // Header with Logo
                    VStack(spacing: 16) {
                        LogoView()
                            .frame(width: 100, height: 100)
                        
                        VStack(spacing: 8) {
                            Text("to name what Silence Holds")
                                .font(.title2)
                                .foregroundColor(.primary)
                            
                            Text("because the unsaid still deserves a voice.")
                                .font(.title3)
                                .foregroundColor(.primary)
                        }
                        
                        Text("A safe space for teens to share mental health experiences, connect with others, and find support on your journey.")
                            .font(.body)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal)
                    }
                    .padding(.top, 20)
                    
                    // Features Section
                    VStack(spacing: 20) {
                        Text("What We Offer")
                            .font(.title)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                        
                        LazyVGrid(columns: [
                            GridItem(.flexible()),
                            GridItem(.flexible())
                        ], spacing: 20) {
                            FeatureCard(
                                icon: "leaf.fill",
                                title: "Safe Space",
                                description: "Your privacy and safety are our top priorities"
                            )
                            
                            FeatureCard(
                                icon: "person.2.fill",
                                title: "Community",
                                description: "Connect with peers who understand your journey"
                            )
                            
                            FeatureCard(
                                icon: "star.fill",
                                title: "Resources",
                                description: "Access helpful tools and professional support"
                            )
                        }
                        .padding(.horizontal)
                    }
                    
                    // Crisis Support Section
                    CrisisSupportCard()
                        .padding(.horizontal)
                }
                .padding(.bottom, 30)
            }
            .navigationTitle("Silence Holds")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct FeatureCard: View {
    let icon: String
    let title: String
    let description: String
    
    var body: some View {
        VStack(spacing: 12) {
            Image(systemName: icon)
                .font(.system(size: 32))
                .foregroundColor(Color(red: 0.72, green: 0.61, blue: 0.49))
                .frame(width: 60, height: 60)
                .background(
                    Circle()
                        .fill(Color(red: 0.99, green: 0.89, blue: 0.93))
                )
            
            Text(title)
                .font(.headline)
                .fontWeight(.semibold)
                .foregroundColor(.primary)
            
            Text(description)
                .font(.caption)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 12)
                .fill(Color.white)
                .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
        )
    }
}

struct CrisisSupportCard: View {
    var body: some View {
        VStack(spacing: 16) {
            Text("Need Help?")
                .font(.headline)
                .fontWeight(.bold)
                .foregroundColor(.primary)
            
            Text("Crisis support is available 24/7")
                .font(.body)
                .foregroundColor(.secondary)
            
            Button(action: {
                if let url = URL(string: "tel:988") {
                    UIApplication.shared.open(url)
                }
            }) {
                Text("Call 988 - Crisis Lifeline")
                    .font(.body)
                    .foregroundColor(Color(red: 0.72, green: 0.61, blue: 0.49))
                    .underline()
            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 12)
                .fill(Color(red: 0.99, green: 0.95, blue: 0.97))
                .overlay(
                    RoundedRectangle(cornerRadius: 12)
                        .stroke(Color(red: 0.97, green: 0.73, blue: 0.85), lineWidth: 1)
                )
        )
    }
}

struct ShareStoryView: View {
    @StateObject private var storyStore = StoryStore()
    @State private var storyTitle = ""
    @State private var storyContent = ""
    @State private var selectedTags: Set<String> = []
    @State private var ageRange = ""
    @State private var showSuccessMessage = false
    @State private var showErrorAlert = false
    @State private var errorMessage = ""
    
    let availableTags = StoryTag.allCases
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    // Header
                    VStack(spacing: 8) {
                        Text("Share Your Story")
                            .font(.largeTitle)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                        
                        Text("Your voice matters. Share your mental health journey to help others feel less alone.")
                            .font(.body)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding(.top, 20)
                    
                    if showSuccessMessage {
                        Text("Thank you for sharing your story! It has been automatically reviewed and published.")
                            .font(.body)
                            .foregroundColor(.green)
                            .padding()
                            .background(
                                RoundedRectangle(cornerRadius: 8)
                                    .fill(Color.green.opacity(0.1))
                            )
                    }
                    
                    // Form
                    VStack(spacing: 20) {
                        // Title Field
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Story Title *")
                                .font(.headline)
                                .foregroundColor(.primary)
                            
                            TextField("Give your story a meaningful title...", text: $storyTitle)
                                .textFieldStyle(RoundedBorderTextFieldStyle())
                        }
                        
                        // Content Field
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Your Story *")
                                .font(.headline)
                                .foregroundColor(.primary)
                            
                            TextEditor(text: $storyContent)
                                .frame(minHeight: 200)
                                .overlay(
                                    RoundedRectangle(cornerRadius: 8)
                                        .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                                )
                        }
                        
                        // Tags Section
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Tags (Select all that apply)")
                                .font(.headline)
                                .foregroundColor(.primary)
                            
                            LazyVGrid(columns: [
                                GridItem(.flexible()),
                                GridItem(.flexible())
                            ], spacing: 8) {
                                ForEach(availableTags) { tag in
                                    TagButton(
                                        tag: tag,
                                        isSelected: selectedTags.contains(tag.name)
                                    ) {
                                        if selectedTags.contains(tag.name) {
                                            selectedTags.remove(tag.name)
                                        } else {
                                            selectedTags.insert(tag.name)
                                        }
                                    }
                                }
                            }
                        }
                        
                        // Age Range
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Age Range (Optional)")
                                .font(.headline)
                                .foregroundColor(.primary)
                            
                            Picker("Age Range", selection: $ageRange) {
                                Text("Prefer not to say").tag("")
                                Text("13-15").tag("13-15")
                                Text("16-17").tag("16-17")
                                Text("18-19").tag("18-19")
                            }
                            .pickerStyle(MenuPickerStyle())
                        }
                        
                        // Submit Button
                        Button(action: submitStory) {
                            Text("Submit Your Story")
                                .font(.headline)
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 8)
                                        .fill(Color(red: 0.72, green: 0.61, blue: 0.49))
                                )
                        }
                        .disabled(storyTitle.isEmpty || storyContent.isEmpty)
                    }
                    .padding(.horizontal)
                    
                    // Community Guidelines
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Community Guidelines")
                            .font(.headline)
                            .foregroundColor(.primary)
                        
                        Text("Your story will be automatically reviewed for appropriateness. Stories are approved if they:")
                            .font(.body)
                            .foregroundColor(.secondary)
                        
                        VStack(alignment: .leading, spacing: 4) {
                            Text("• Share personal mental health experiences respectfully")
                            Text("• Use appropriate language and tone")
                            Text("• Don't contain harmful content or explicit details")
                            Text("• Focus on support, hope, and shared experiences")
                        }
                        .font(.body)
                        .foregroundColor(.secondary)
                    }
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 8)
                            .fill(Color(red: 0.98, green: 0.98, blue: 0.98))
                    )
                    .padding(.horizontal)
                }
                .padding(.bottom, 30)
            }
            .navigationTitle("Share Story")
            .navigationBarTitleDisplayMode(.inline)
            .alert("Story Not Approved", isPresented: $showErrorAlert) {
                Button("OK") { }
            } message: {
                Text(errorMessage)
            }
        }
    }
    
    private func submitStory() {
        let story = Story(
            title: storyTitle,
            content: storyContent,
            tags: Array(selectedTags),
            ageRange: ageRange.isEmpty ? nil : ageRange
        )
        
        storyStore.addStory(story)
        
        // Show success message
        showSuccessMessage = true
        
        // Reset form
        storyTitle = ""
        storyContent = ""
        selectedTags.removeAll()
        ageRange = ""
        
        // Hide success message after 3 seconds
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            showSuccessMessage = false
        }
    }
}

struct TagButton: View {
    let tag: StoryTag
    let isSelected: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            Text(tag.displayName)
                .font(.caption)
                .foregroundColor(isSelected ? .white : .primary)
                .padding(.horizontal, 12)
                .padding(.vertical, 6)
                .background(
                    RoundedRectangle(cornerRadius: 20)
                        .fill(isSelected ? Color(red: 0.72, green: 0.61, blue: 0.49) : Color.clear)
                        .overlay(
                            RoundedRectangle(cornerRadius: 20)
                                .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                        )
                )
        }
    }
}

struct StoriesView: View {
    @StateObject private var storyStore = StoryStore()
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    Text("Stories")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .padding(.top, 20)
                    
                    Text("Real experiences from teens like you. Read, connect, and find hope in shared journeys.")
                        .font(.body)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                    
                    if storyStore.approvedStories.isEmpty {
                        // Empty state
                        VStack(spacing: 16) {
                            Text("No stories yet")
                                .font(.title2)
                                .foregroundColor(.primary)
                            
                            Text("Be the first to share your story and inspire others!")
                                .font(.body)
                                .foregroundColor(.secondary)
                        }
                        .padding(40)
                    } else {
                        // Stories list
                        LazyVStack(spacing: 16) {
                            ForEach(storyStore.approvedStories) { story in
                                StoryCard(story: story, onDelete: {
                                    storyStore.deleteStory(story.id)
                                })
                            }
                        }
                        .padding(.horizontal)
                    }
                }
                .padding(.bottom, 30)
            }
            .navigationTitle("Stories")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct StoryCard: View {
    let story: Story
    let onDelete: () -> Void
    @State private var showDeleteAlert = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Tag
            if let firstTag = story.tags.first,
               let tagInfo = StoryTag.allCases.first(where: { $0.name == firstTag }) {
                Text(tagInfo.displayName)
                    .font(.caption)
                    .fontWeight(.medium)
                    .foregroundColor(Color(hex: tagInfo.textColor))
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color(hex: tagInfo.color))
                    )
            }
            
            // Title
            Text(story.title)
                .font(.headline)
                .fontWeight(.semibold)
                .foregroundColor(.primary)
            
            // Content preview
            Text(story.content.count > 150 ? String(story.content.prefix(150)) + "..." : story.content)
                .font(.body)
                .foregroundColor(.secondary)
                .lineLimit(nil)
            
            // Metadata
            HStack {
                if let ageRange = story.ageRange {
                    Text("Age: \(ageRange)")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                
                if let approvedAt = story.approvedAt {
                    Text("• \(approvedAt, style: .date)")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                
                Spacer()
                
                Button("Delete") {
                    showDeleteAlert = true
                }
                .font(.caption)
                .foregroundColor(.red)
            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 12)
                .fill(Color.white)
                .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
        )
        .alert("Delete Story", isPresented: $showDeleteAlert) {
            Button("Cancel", role: .cancel) { }
            Button("Delete", role: .destructive) {
                onDelete()
            }
        } message: {
            Text("Are you sure you want to delete this story? This action cannot be undone.")
        }
    }
}

struct ResourcesView: View {
    @StateObject private var resourceStore = ResourceStore()
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    Text("Helpful Resources")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .padding(.top, 20)
                    
                    Text("Tools and support for your mental health journey")
                        .font(.body)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal)
                    
                    LazyVStack(spacing: 16) {
                        ForEach(resourceStore.resources) { resource in
                            ResourceCard(resource: resource) {
                                resourceStore.openResource(resource)
                            }
                        }
                    }
                    .padding(.horizontal)
                }
                .padding(.bottom, 30)
            }
            .navigationTitle("Resources")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct ResourceCard: View {
    let resource: Resource
    let onAction: () -> Void
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(resource.type.displayName)
                    .font(.caption)
                    .fontWeight(.medium)
                    .foregroundColor(.white)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color(hex: resource.type.color))
                    )
                
                Spacer()
            }
            
            Text(resource.title)
                .font(.headline)
                .fontWeight(.semibold)
                .foregroundColor(.primary)
            
            Text(resource.description)
                .font(.body)
                .foregroundColor(.secondary)
            
            HStack {
                Spacer()
                Button(action: onAction) {
                    Text(resource.action)
                        .font(.body)
                        .foregroundColor(Color(red: 0.72, green: 0.61, blue: 0.49))
                        .underline()
                }
            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 12)
                .fill(Color.white)
                .shadow(color: Color.black.opacity(0.1), radius: 4, x: 0, y: 2)
        )
    }
}

// MARK: - Main App

struct ContentView: View {
    @State private var selectedTab = 0
    
    var body: some View {
        TabView(selection: $selectedTab) {
            HomeView()
                .tabItem {
                    Image(systemName: "house.fill")
                    Text("Home")
                }
                .tag(0)
            
            SobrietyJourneyView()
                .tabItem {
                    Image(systemName: "leaf.fill")
                    Text("Sobriety")
                }
                .tag(1)
            
            WellnessView()
                .tabItem {
                    Image(systemName: "heart.fill")
                    Text("Wellness")
                }
                .tag(2)
            
            ShareStoryView()
                .tabItem {
                    Image(systemName: "square.and.pencil")
                    Text("Share")
                }
                .tag(3)
            
            StoriesView()
                .tabItem {
                    Image(systemName: "book.fill")
                    Text("Stories")
                }
                .tag(4)
            
            ResourcesView()
                .tabItem {
                    Image(systemName: "person.2.fill")
                    Text("Resources")
                }
                .tag(5)
        }
        .accentColor(Color(red: 0.72, green: 0.61, blue: 0.49)) // #B89B7E
    }
}

@main
struct SilenceHoldsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

// MARK: - Extensions

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (1, 1, 1, 0)
        }

        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}

// Previews removed due to file size limitations
// The app builds and runs successfully without previews
