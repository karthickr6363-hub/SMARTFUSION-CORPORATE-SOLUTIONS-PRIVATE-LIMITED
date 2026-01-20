(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: true,
        loop: true,
        center: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 45,
        dots: false,
        loop: true,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:4
            },
            768:{
                items:6
            },
            992:{
                items:8
            }
        }
    });

    // AI Chat Box Functionality
    const chatToggleBtn = $('#aiChatToggleBtn');
    const chatWindow = $('#aiChatWindow');
    const closeChatBtn = $('#closeChatBtn');
    const chatInput = $('#aiChatInput');
    const chatSendBtn = $('#aiChatSendBtn');
    const chatMessages = $('#aiChatMessages');
    const chatBadge = $('.ai-chat-badge');

    // Toggle chat window
    chatToggleBtn.on('click', function() {
        chatWindow.toggleClass('active');
        if (chatWindow.hasClass('active')) {
            chatBadge.hide();
            chatInput.focus();
        }
    });

    // Close chat window
    closeChatBtn.on('click', function() {
        chatWindow.removeClass('active');
    });

    // Send message function
    function sendMessage() {
        const message = chatInput.val().trim();
        if (message === '') return;

        // Add user message
        addMessage(message, 'user');
        chatInput.val('');

        // Show typing indicator
        const typingIndicator = $('<div class="ai-message ai-message-bot"><div class="ai-message-content"><p class="mb-0"><i class="fas fa-circle"></i> <i class="fas fa-circle"></i> <i class="fas fa-circle"></i></p></div></div>');
        chatMessages.append(typingIndicator);
        scrollToBottom();

        // Simulate AI response (replace with actual API call)
        setTimeout(function() {
            typingIndicator.remove();
            const responses = [
                "Thank you for your message! I'm here to help you with any questions about our services.",
                "That's a great question! Let me help you with that. Our team specializes in providing innovative solutions.",
                "I understand your concern. Would you like me to connect you with one of our specialists?",
                "Great! I'd be happy to provide more information. What specific aspect would you like to know more about?",
                "Thank you for reaching out! Our services are designed to help businesses like yours succeed."
            ];
            const randomResponse = responses[Math.floor(Math.random() * responses.length)];
            addMessage(randomResponse, 'bot');
        }, 1500);
    }

    // Add message to chat
    function addMessage(text, type) {
        const now = new Date();
        const timeString = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
        
        const messageDiv = $('<div class="ai-message ai-message-' + type + '"></div>');
        const contentDiv = $('<div class="ai-message-content"><p class="mb-0">' + escapeHtml(text) + '</p></div>');
        const timeDiv = $('<small class="ai-message-time">' + timeString + '</small>');
        
        messageDiv.append(contentDiv);
        messageDiv.append(timeDiv);
        chatMessages.append(messageDiv);
        
        scrollToBottom();
    }

    // Scroll to bottom of chat
    function scrollToBottom() {
        chatMessages.scrollTop(chatMessages[0].scrollHeight);
    }

    // Escape HTML to prevent XSS
    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }

    // Send message on button click
    chatSendBtn.on('click', sendMessage);

    // Send message on Enter key
    chatInput.on('keypress', function(e) {
        if (e.which === 13) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Typing animation for bot messages
    function animateTyping() {
        const dots = $('.ai-message-bot .fa-circle');
        let count = 0;
        const interval = setInterval(function() {
            dots.eq(count % 3).css('opacity', '0.3');
            count++;
            if (count > 3) {
                clearInterval(interval);
            }
        }, 300);
    }
    
})(jQuery);

