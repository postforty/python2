document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM Content Loaded: Script is running.');

    const cardContainer = document.getElementById('restaurant-cards');
    const modal = document.getElementById('modal');
    const closeModalButton = document.getElementById('close-modal');
    const filtersContainer = document.getElementById('category-filters');

    let allRestaurants = []; // To store all restaurant data

    if (!cardContainer || !modal || !closeModalButton || !filtersContainer) {
        console.error('Error: A critical element was not found in the DOM!');
        return;
    }

    // Fetch data, set up filters, and build cards
    fetch('list.json')
        .then(response => {
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            allRestaurants = data.filter(item => item.title); // Store only crawled items
            console.log('All crawled restaurants:', allRestaurants);
            
            setupCategoryFilters();
            renderCards(allRestaurants); // Initial render of all cards
        })
        .catch(error => {
            console.error('Error fetching restaurant data:', error);
            cardContainer.innerHTML = '<p class="error-message">데이터를 불러오는 데 실패했습니다. 콘솔을 확인하세요.</p>';
        });

    function setupCategoryFilters() {
        const categories = ['전체', ...new Set(allRestaurants.map(r => r.category).filter(Boolean))];
        console.log('Found categories:', categories);
        
        filtersContainer.innerHTML = '';
        categories.forEach(category => {
            const button = document.createElement('button');
            button.className = 'filter-btn';
            button.textContent = category;
            button.dataset.category = category;
            if (category === '전체') {
                button.classList.add('active');
            }
            filtersContainer.appendChild(button);
        });

        filtersContainer.addEventListener('click', (e) => {
            if (e.target.tagName !== 'BUTTON') return;

            // Update active button style
            filtersContainer.querySelector('.active').classList.remove('active');
            e.target.classList.add('active');

            const selectedCategory = e.target.dataset.category;
            console.log('Filter clicked:', selectedCategory);

            if (selectedCategory === '전체') {
                renderCards(allRestaurants);
            } else {
                const filteredRestaurants = allRestaurants.filter(r => r.category === selectedCategory);
                renderCards(filteredRestaurants);
            }
        });
    }
    
    function renderCards(restaurants) {
        cardContainer.innerHTML = '';
        if (restaurants.length === 0) {
            cardContainer.innerHTML = '<p>해당 카테고리의 식당이 없습니다.</p>';
            return;
        }
        restaurants.forEach(restaurant => {
            const card = createRestaurantCard(restaurant);
            card.addEventListener('click', () => openModal(restaurant));
            cardContainer.appendChild(card);
        });
    }

    function createRestaurantCard(restaurant) {
        const card = document.createElement('div');
        card.className = 'card';

        const img = document.createElement('img');
        img.className = 'card-img';
        img.src = restaurant.imageUrl || 'https://via.placeholder.com/300x200.png?text=No+Image';
        img.alt = restaurant.title;

        const content = document.createElement('div');
        content.className = 'card-content';

        const title = document.createElement('h3');
        title.className = 'card-title';
        title.textContent = restaurant.title;

        const category = document.createElement('p');
        category.className = 'card-category';
        category.textContent = restaurant.category || '기타';

        content.appendChild(title);
        content.appendChild(category);
        card.appendChild(img);
        card.appendChild(content);

        return card;
    }

    function openModal(restaurant) {
        console.log('openModal called for:', restaurant.title);

        document.getElementById('modal-img').src = restaurant.imageUrl || 'https://via.placeholder.com/600x250.png?text=No+Image';
        document.getElementById('modal-title').textContent = restaurant.title || '제목 없음';
        document.getElementById('modal-category').textContent = restaurant.category || '기타';
        document.getElementById('modal-description').textContent = restaurant.description || '설명 없음';
        document.getElementById('modal-visitor-reviews').textContent = restaurant.visitorReviews || '정보 없음';
        document.getElementById('modal-blog-reviews').textContent = restaurant.blogReviews || '정보 없음';
        document.getElementById('modal-address').textContent = restaurant.address || '정보 없음';
        document.getElementById('modal-phone').textContent = restaurant.phone || '정보 없음';
        document.getElementById('modal-hours').textContent = (restaurant.businessHours || '정보 없음').replace(/\\n/g, ' ');

        const mapButton = document.getElementById('modal-map-button');
        if (restaurant.url) {
            mapButton.href = restaurant.url;
            mapButton.style.display = 'inline-block';
        } else {
            mapButton.style.display = 'none';
        }

        modal.classList.add('active');
    }

    function closeModal() {
        if (modal) modal.classList.remove('active');
    }

    // Event listeners for closing the modal
    closeModalButton.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) closeModal();
    });
});
