from django.db.models.aggregates import Avg
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """ Add a review to a product/trip """

    if request.user.is_authenticated:
        if request.method == "POST":
            product = get_object_or_404(Product, pk=product_id)
            user = UserProfile.objects.get(user=request.user)
            review_form = ReviewForm(request.POST)
            # check if user already added a review
            added_review = Review.objects.filter(user=user, product=product)
            if added_review.exists():
                messages.error(request, 'You already reviewed this product. \
                    To change your review click the edit button \
                        on your review.')
            else:
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.product = product
                    review.user = user
                    review.save()

                    # Recalculate rating
                    reviews = Review.objects.filter(product=product)
                    average_rating = (reviews.aggregate(Avg('rating'))
                                      ['rating__avg'])
                    product.rating = average_rating
                    product.save()

                    messages.success(request, 'Review succesfully added!')
                else:
                    messages.error(request, 'Failed to add review. \
                        Please ensure the form is valid.')
            return redirect(reverse('product_detail', args=[product.id]))

    else:
        messages.error(request, 'Sorry, only logged in users can \
            leave a review.')
        return redirect(reverse('login'))


@login_required
def edit_review(request, review_id):
    """ Edit a review  """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can \
            edit a review.')
        return redirect(reverse('login'))

    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        if request.method == "POST":
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid:
                form.save()

                # Recalculate rating
                product = Product.objects.get(name=review.product)
                reviews = Review.objects.filter(product=product)
                average_rating = (reviews.aggregate(Avg('rating'))
                                  ['rating__avg'])
                product.rating = average_rating
                product.save()
                messages.success(request, 'Your review is \
                    edited successfully!')

            else:
                messages.error(request, 'Failed to edit review. \
                    Please ensure the form is valid.')

            return redirect(reverse(
                            'product_detail', args=[review.product.id]))
        else:
            form = ReviewForm(instance=review)
            messages.info(
                request, f'You are editing your review: {review.title}')

        template = 'reviews/edit_review.html'
        context = {
            'form': form,
            'review': review,
        }

        return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review on the product page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can \
            delete a review.')
        return redirect(reverse('login'))

    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)

        if request.user:
            review.delete()

            # Recalculate rating
            product = Product.objects.get(name=review.product)
            reviews = Review.objects.filter(product=product)
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = average_rating
            product.save()

            messages.success(request, 'Your review has been deleted.')
            return redirect(reverse('product_detail',
                                    args=[review.product.id]))
        else:
            messages.error(request, 'Cannot delete review, \
                this is not your review')
            return redirect(reverse('product_detail',
                                    args=[review.product.id]))
