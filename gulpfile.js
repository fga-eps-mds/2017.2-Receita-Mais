'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var runsequence = require('run-sequence');
var reload = browserSync.reload;

var directoryjs = './medical_prescription/**/*.js'
var directorycss = './medical_prescription/**/*.css'
var directoryhtml = './medical_prescription/**/*.html'

var dist = "./dist"

gulp.task('browserSync', function() {
  browserSync.init({
    open: false,
    notify: false,
    proxy: 'localhost:8000'
  })
});

gulp.task('watch', function() {
  gulp.watch(directoryjs,['files']);
  gulp.watch(directoryhtml,['files']);
  gulp.watch(directorycss,['files']);
});

gulp.task('reload', function() {
  gulp.watch(directoryjs).on('change', browserSync.reload);
  gulp.watch(directoryhtml).on('change', browserSync.reload);
  gulp.watch(directorycss).on('change', browserSync.reload);
});

gulp.task('files', function() {
  return gulp.src(directory)
    .pipe(gulp.dest(dist));
});

gulp.task('build', function(cb) {
  runsequence('files', cb);
});

gulp.task('default',['browserSync', 'watch','reload']);
